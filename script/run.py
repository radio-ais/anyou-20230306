from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.model_selection import GridSearchCV, cross_validate, StratifiedKFold, RepeatedStratifiedKFold


import pandas as pd
import numpy as np

window_type = "nw"
rf_coif_path = "output/fe/" + "-".join(["fe", window_type]) + ".csv"
rf_bior_path = "output/fe/" + "-".join(["fe", window_type, "bior1.1"]) + ".csv"
rf_sym_path = "output/fe/" + "-".join(["fe", window_type, "sym2"]) + ".csv"

cl_data_path = "output/clinical/RP_label_v3.csv"
df_data_path = "output/dvh/"

# sample:
# - Radiomics Features
# - Dosimetric Features
# - Clinical Features

# ML Pipeline
# 1. Prepare Data: use make_column_selector in pipeline implementation
#   - load radiomics features: starts with rf_*
#   - load subset of dosimetric features: starts with df_*
#   - load clinical features: starts with cl_*
# 2. Nested Cross-validation
#   - Repeats only on outer layer
# 3. Post-hoc analysis

"""
rf_preprocessor = ColumnTransformer()
df_preprocessor = ColumnTransformer()
cl_preprocessor = ColumnTransformer()

preprocessor = ColumnTransformer([
    ('rf_preprocessing', rf_preprocessor, make_column_selector(pattern="rf-*")),
    ('df_preprocessing', df_preprocessor, make_column_selector(pattern='df-*')),
    ('cl_preprocessing', cl_preprocessor, make_column_selector(pattern='cl-*'))
])

classifiers = FeatureUnion([
    ('lr_l1', LogisticRegression()),
    ('lr_l2', LogisticRegression()),
    ('svc', SVC()),
    ('rf', RandomForestClassifier())
])

pipe = Pipeline([
    ('preprocess', preprocessor),
    ('clf', classifiers)
])
"""
def dataloader():
    def wavelet_named(path, name):
        rf_data = pd.read_csv(path)
        rf_start_index = [v for v, c in enumerate(rf_data.columns) if "diagnostics" in c][-1] + 1
        rf_data.drop(rf_data.columns[1:rf_start_index], axis=1, inplace=True)
        rf_data.columns = ["_".join([name, cn]) if "wavelet" in cn else cn for cn in rf_data.columns]
        return rf_data
    
    rf_coif = wavelet_named(rf_coif_path, "coif1")
    rf_bior = wavelet_named(rf_bior_path, "bior1.1")
    #rf_sym = wavelet_named(rf_sym_path, "sym2")

    rf_data = rf_coif.merge(rf_bior, on="ID", how="left")
    #rf_data = rf_data.join(rf_sym, on="ID", how="left")

    rf_data.columns = ["rf-" + cn if "ID" != cn else cn for cn in rf_data.columns ]
    
    
    df_data = None # read df_data

    cl_data = pd.read_csv(cl_data_path)

    
    return X, y

inner_grid = {

}

inner_params = {

}

outer_params = {
    
}

if __name__ == "__main__":
    X, y = dataloader()
    grid = GridSearchCV(pipe, inner_grid, **inner_params)
    result = cross_validate(grid, X, y, **outer_params)
