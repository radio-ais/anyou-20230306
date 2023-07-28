# coding: utf-8
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Ctab(Base):
	__tablename__ = 'ctab'

	id = Column(BIGINT(20), primary_key=True)
	createdat = Column(DateTime, server_default=text("current_timestamp()"))
	updatedat = Column(DateTime)
	sct_ab_desc = Column(String(20))
	sct_ab_num = Column(String(20))
	sct_epi_loc = Column(String(20))
	sct_long_dia = Column(String(20))
	sct_margins = Column(String(20))
	sct_perp_dia = Column(String(20))
	sct_pre_att = Column(String(20))
	study_yr = Column(String(20))
	sct_slice_num = Column(String(20))
	sct_found_after_comp = Column(String(100))
	pid = Column(String(20), index=True)
	dataset_version = Column(String(100))


class Ctabc(Base):
	__tablename__ = 'ctabc'

	id = Column(BIGINT(20), primary_key=True)
	createdat = Column(DateTime, server_default=text("current_timestamp()"))
	updatedat = Column(DateTime)
	study_yr = Column(String(40))
	sct_ab_preexist = Column(String(40))
	pid = Column(String(40), index=True)
	sct_ab_attn = Column(String(40))
	sct_ab_gwth = Column(String(40))
	sct_ab_invg = Column(String(40))
	sct_ab_num = Column(String(40))
	sct_ab_code = Column(String(40))
	dataset_version = Column(String(40))
	visible_days = Column(String(40))


class Ctabcwide(Base):
	__tablename__ = 'ctabcwide'

	id = Column(BIGINT(20), primary_key=True)
	createdat = Column(DateTime, server_default=text("current_timestamp()"))
	updatedat = Column(DateTime)
	study_yr = Column(String(40))
	sct_ab_preexist = Column(String(40))
	pid = Column(String(40))
	sct_ab_attn = Column(String(40))
	sct_ab_gwth = Column(String(40))
	sct_ab_invg = Column(String(40))
	sct_ab_num = Column(String(40))
	sct_ab_code = Column(String(40))
	dataset_version = Column(String(40))
	visible_days = Column(String(40))
	studyyr = Column(String(40))
	sctabpreexist = Column(String(40))
	sctabattn = Column(String(40))
	sctabgwth = Column(String(40))
	sctabinvg = Column(String(40))
	sctabnum = Column(String(40))
	sctabcode = Column(String(40))
	datasetversion = Column(String(40))
	visibledays = Column(String(40))


class Ctabwide(Base):
	__tablename__ = 'ctabwide'

	id = Column(BIGINT(20), primary_key=True)
	createdat = Column(DateTime, server_default=text("current_timestamp()"))
	updatedat = Column(DateTime)
	sct_ab_desc = Column(String(20))
	sct_ab_num = Column(String(20))
	sct_epi_loc = Column(String(20))
	sct_long_dia = Column(String(20))
	sct_margins = Column(String(20))
	sct_perp_dia = Column(String(20))
	sct_pre_att = Column(String(20))
	study_yr = Column(String(20))
	sct_slice_num = Column(String(20))
	sct_found_after_comp = Column(String(100))
	pid = Column(String(20))
	dataset_version = Column(String(100))
	sctabdesc = Column(String(20))
	sctabnum = Column(String(20))
	sctepiloc = Column(String(20))
	sctlongdia = Column(String(20))
	sctmargins = Column(String(20))
	sctperpdia = Column(String(20))
	sctpreatt = Column(String(20))
	studyyr = Column(String(20))
	sctslicenum = Column(INTEGER(11))
	sctfoundaftercomp = Column(String(100))
	datasetversion = Column(String(100))


class Label(Base):
	__tablename__ = 'labels'

	id = Column(BIGINT(20), primary_key=True)
	createdat = Column(DateTime, server_default=text("current_timestamp()"))
	updatedat = Column(DateTime)
	pid = Column(String(40), unique=True)
	posneg = Column(String(10))


class Metadatum(Base):
	__tablename__ = 'metadata'

	id = Column(BIGINT(20), primary_key=True)
	createdat = Column(DateTime, server_default=text("current_timestamp()"))
	updatedat = Column(DateTime)
	setnumber = Column(String(20))
	seriesuid = Column(String(100), index=True)
	collection_ = Column(String(20))
	thirdpartyanalysis = Column(String(100))
	datadescriptionuri = Column(String(100))
	subjectid = Column(String(100), index=True)
	studyuid = Column(String(100))
	studydescription = Column(String(100))
	studydate = Column(String(100))
	seriesdescription = Column(String(100))
	manufacturer = Column(String(100))
	modality = Column(String(100))
	sopclassname = Column(String(100))
	sopclassiod = Column(String(100))
	numberofimages = Column(String(30))
	filesize = Column(String(100))
	filelocation = Column(String(200))
	downloadtimestamp = Column(String(30))
	unkown1 = Column(String(10))
	unkown2 = Column(String(10))
	numberofimagesi = Column(INTEGER(11))
	sigsha = Column(String(60))
	pid = Column(String(20))
