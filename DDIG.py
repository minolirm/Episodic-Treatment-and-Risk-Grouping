import time
import warnings
from datetime import datetime
import numpy as np
import pandas as pd

import config
from app.clm_file_creator import clm_file_creator
from app.cntrl_rprt_creator import control_report_creator
from app.conf_file_creator import conf_file_creator
from app.smy_file_creator import smy_file_creator
from app.src import stringify_columns, ddi_ungroup_num_lst, lst_of_ddi_in_cols, lst_of_ddi_out_cols, ddig_ref_cols, \
    lst_cs_cols
from app.utils import read_json


warnings.filterwarnings("ignore")

start_time = time.time()
start_date = datetime.now()

custom_date_parser = lambda x: datetime.strptime(x, "%m/%d/%Y")

clm_in_df = pd.read_csv(
    config.PATH_INPUT_CLAIMS,
    usecols=lst_of_ddi_in_cols,
    parse_dates=["FirstDateOfService", "LastDateOfService"],
    date_parser=custom_date_parser
)

enrlmnt_in_df = pd.read_csv(
    config.PATH_INPUT_ENROLMENT,
    parse_dates=["EffectiveDate", "TerminateDate"],
    date_parser=custom_date_parser
)

mem_in_df = pd.read_csv(config.PATH_INPUT_MEMBERS)

clm_mem_count = len(clm_in_df["FamilyID"].unique().tolist())
in_clm_count = clm_in_df.shape[0]
in_mem_count = mem_in_df.shape[0]
in_enrlmnt_count = enrlmnt_in_df.shape[0]

clm_in_df.fillna(np.nan)
enrlmnt_in_df.fillna(np.nan)

clm_in_df = clm_in_df.groupby("FamilyID", as_index=False).apply(
    lambda x: x.sort_values("FirstDateOfService")).reset_index(drop=True)

clm_in_df = clm_in_df.groupby(["FamilyID", "FirstDateOfService"], as_index=False).apply(
    lambda x: x.sort_values("LastDateOfService")).reset_index(drop=True)

clm_in_df = clm_in_df.groupby(["FamilyID", "FirstDateOfService", "LastDateOfService"], as_index=False).apply(
    lambda x: x.sort_values("UniqueRecordID")).reset_index(drop=True)

ddi_grouper_df = pd.read_csv(config.PATH_MAIN_REF_GROUPER, usecols=ddig_ref_cols)

icd_10_lst = ddi_grouper_df["ICD10_Code"].tolist()
icd_10_set = set(icd_10_lst)
ddi_hd_lst = ddi_grouper_df["DDI_Health_State_Domain_Name"].tolist()
ddi_base_class_lst = ddi_grouper_df["DDIG_Base_Class"].tolist()
ddig_cp_lst = ddi_grouper_df["Clean_Period"].tolist()
ddi_comp_lst = ddi_grouper_df["Complication_Status"].tolist()

ndc_dict = read_json(config.PATH_MAIN_REF_ALL_NDC)

proc_dic = read_json(config.PATH_MAIN_REF_PROCEDURE_CODES)

cpt_rt_dic = read_json(config.PATH_MAIN_REF_CPT_RECORD_TYPE)

cpt_I_rt_dic = read_json(config.PATH_REF_CPT_CATEGORY_I_RT)

m_rt_dic = read_json(config.PATH_MAIN_REF_M_CODE_RECORD_TYPE)

rad_df = pd.read_csv(config.PATH_REF_RAD_PROC)
rad_proc_lst = rad_df["Procedure_Code"].tolist()

lab_df = pd.read_csv(config.PATH_REF_LAB_PROC)
lab_proc_lst = lab_df["Procedure_Code"].tolist()

rev_dic = read_json(config.PATH_MAIN_REF_ALL_REVENUE_CODES)

rev_rt_dic = read_json(config.PATH_MAIN_REF_REVENUE_CODE_RECORD_TYPE)

z_rt_dic = read_json(config.PATH_MAIN_REF_Z_RECORD_TYPE)

clm_out_df = clm_file_creator(
    clm_in_df,
    enrlmnt_in_df,
    stringify_columns,
    config.PATH_OUTPUT_DDI_G_CLAIM,
    ddi_ungroup_num_lst,
    icd_10_set,
    proc_dic,
    cpt_rt_dic,
    cpt_I_rt_dic,
    m_rt_dic,
    rev_dic,
    rev_rt_dic,
    z_rt_dic,
    ndc_dict,
    rad_proc_lst,
    lab_proc_lst,
    lst_of_ddi_out_cols,
    lst_cs_cols
)

conf_df = conf_file_creator(clm_out_df, config.PATH_OUTPUT_DDI_G_CONFINEMENT)
smy_df = smy_file_creator(clm_out_df, config.PATH_OUTPUT_DDI_G_SUMMARY)

end_date = datetime.now()

external_validation_file = control_report_creator(
    config.VERSION_NAME,
    start_date,
    end_date,
    in_clm_count,
    in_mem_count,
    in_enrlmnt_count,
    clm_mem_count,
    clm_out_df,
    smy_df,
    conf_df,
    config.PATH_OUTPUT_DDI_G_CONTROL_REPORT,
    config.PATH_INPUT_CLAIMS,
    config.PATH_INPUT_MEMBERS,
    config.PATH_INPUT_ENROLMENT,
    config.PATH_OUTPUT_DDI_G_CLAIM,
    config.PATH_OUTPUT_DDI_G_SUMMARY,
    config.PATH_OUTPUT_DDI_G_CONFINEMENT,
    ddi_ungroup_num_lst)

print("\n DDIG whole process is completed....", time.time() - start_time)

