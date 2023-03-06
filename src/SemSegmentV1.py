from pl_bolts.models.vision import SemSegment, UNet
import torch.nn.functional as F
import torch
import torch.nn as nn

class DiceBCELoss(nn.Module):
    def __init__(self, weight=None, size_average=True):
        super(DiceBCELoss, self).__init__()

    def forward(self, inputs, targets, smooth=1):
        
        #comment out if your model contains a sigmoid or equivalent activation layer
        inputs = F.sigmoid(inputs)       
        
        #flatten label and prediction tensors
        inputs = inputs.view(-1)
        targets = targets.view(-1)
        
        intersection = (inputs * targets).sum()                            
        dice_loss = 1 - (2.*intersection + smooth)/(inputs.sum() + targets.sum() + smooth)  
        BCE = F.binary_cross_entropy(inputs, targets, reduction='mean')
        Dice_BCE = BCE + dice_loss
        
        return Dice_BCE

class SemSegmentV1(SemSegment):
	def __init__(
		self, 
		num_classes = 19,
		num_layers = 5,
		features_start = 64,
		bilinear = False,
		ignore_index = 250,
		lr = 0.01,
		input_channels = 1,
		**kwargs):

		super().__init__()

		self.input_channels = input_channels
		self.net = UNet(
						num_classes,
						input_channels=input_channels,
						num_layers=self.num_layers,
						features_start=features_start,
						bilinear=bilinear
						)
		self.loss_fn = DiceBCELoss()

	def training_step(self, batch, batch_idx: int):
            img, mask = batch
            img = img.float()
            #mask = mask.long()
            out = self(img)
            #out = F.sigmoid(out)
            #loss_val = F.cross_entropy(out, mask, ignore_index=self.ignore_index)
            loss_val = self.loss_fn(out, mask)
            log_dict = {"train_loss": loss_val}
            return {"loss": loss_val, "log": log_dict, "progress_bar": log_dict}
	def configure_optimizers(self):
            opt = torch.optim.SGD(self.net.parameters(), lr=self.lr, momentum=0.9)
            sch = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=10)
            return [opt], [sch]
