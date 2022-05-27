"""Monitoring Module to use for IM-FIT"""
from fpdf import FPDF


def create_new_v_and_v_report(
    monitoring_metric_list,
    monitroing_mutant_list,
    monitoring_killed_mutants_output_list,
    monitoring_faults_list,
    monitoring_rosbag_scenarios_list,
):
    """ After all processes are done, IM-FIT creates a V&V report about the processes"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=9)
    v_and_v_report_introduction = """
    The V&V Report Created by IM-FIT
    This reports shows information about AST Diagram of Source Codes, Fault List, Metric List, Rosbag Scenarios, etc.
    Therefore the user can learn about its source codes.

    IM-FIT
    """
    pdf.cell(200, 10, txt=v_and_v_report_introduction, ln=1, align="C")
    pdf.cell(200, 10, txt=monitoring_metric_list, ln=2, align="L")
    pdf.cell(200, 10, txt=monitroing_mutant_list, ln=3, align="L")
    pdf.cell(200, 10, txt=monitoring_killed_mutants_output_list, ln=4, align="L")
    pdf.cell(200, 10, txt=monitoring_faults_list, ln=5, align="L")
    pdf.cell(200, 10, txt=monitoring_rosbag_scenarios_list, ln=6, align="L")
    pdf.output("V&V_Report_by_IM-FIT.pdf")
