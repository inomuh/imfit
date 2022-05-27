"""Scan Process Module to use for IM-FIT"""

import json
import re

# Open code snippet JSON file to use for the processes
def open_code_snip():
    """Code snippet json file is opened to use for code snippet use cases"""
    with open("code_snippets.json", encoding="utf-8") as code_snippets_from_json:
        code_snippet_regex_code = json.load(code_snippets_from_json)

    return code_snippet_regex_code


# Yes Workload, Yes Code Snippet
def take_workload_name_list(workload_data):
    """Workload names are taken by IM-FIT to detect them in the source code"""
    workload_function_name_list = []
    try:
        for i in range(0, len(workload_data["Tasks"])):
            workload_name_from_json = workload_data["Tasks"][i]["Task"]["Task_ID"]
            search_workload_name_from_json = "def " + workload_name_from_json
            workload_function_name_list.append(search_workload_name_from_json)
    except:
        print("Workload Build Error!")

    return workload_function_name_list


def workload_lines(split_text, workload_function_name_list):
    """Detected workload lines are added to the list to use for
    yes workload, yes code snippet use case"""
    painted_lines = []
    for number, line in enumerate(split_text):
        for function_name_from_workload in workload_function_name_list:
            is_function_in_sentence = re.findall(function_name_from_workload, line)
            if is_function_in_sentence:
                while number != 0:
                    leading_spaces = len(split_text[number]) - len(
                        split_text[number].lstrip()
                    )
                    if leading_spaces != 0:
                        painted_lines.append(number)
                        number += 1
                    else:
                        break

    return painted_lines


def find_patterns_yes_wl_yes_cs(added_snippet_regex_length, code_snippet_data_list):
    """Method finds regex codes of the selected code snippets"""
    patterns = []
    code_snippet_regex_code = open_code_snip()
    for i in range(0, added_snippet_regex_length):
        added_snippet_name = code_snippet_regex_code["code_snippets"][i]["Snippets"][
            "Snippet_Name"
        ]
        added_snippet_regex = code_snippet_regex_code["code_snippets"][i]["Snippets"][
            "Regex_Code"
        ]
        for snippet in code_snippet_data_list:
            if snippet == added_snippet_name:
                patterns.append(added_snippet_regex)

    return patterns


def scan_yes_wl_yes_cs(patterns, source_code_list, painted_lines):
    """Scan process applies to the source code according to
    selected workload and selected code snippets"""
    faultable_line_list = []
    faultable_line_number_list = []
    for i in painted_lines:
        detected_parts_list_line = source_code_list[i]
        find_function = re.findall("def:*", detected_parts_list_line)
        find_class = re.findall("class:*", detected_parts_list_line)
        find_import = re.findall("import", detected_parts_list_line)
        find_comment = re.findall("#", detected_parts_list_line)
        if (
            not find_function
            and not find_class
            and not find_import
            and not find_comment
        ):
            for pattern in patterns:
                result = re.findall(pattern, detected_parts_list_line, re.MULTILINE)
                if result:

                    faultable_line_list.append(detected_parts_list_line)
                    faultable_line_number_list.append(i)

    return faultable_line_list, faultable_line_number_list


# No Workload, No Code Snippet
def take_code_snippet_regex_code_list():
    """Method takes all regex codes from json file to use scan process
    for no workload, no code snippet use case"""
    code_snippet_regex_code_list = []

    code_snippet_regex_code = open_code_snip()

    added_snippet_regex_length = len(code_snippet_regex_code["code_snippets"])
    for i in range(0, added_snippet_regex_length):
        added_snippet_regex = code_snippet_regex_code["code_snippets"][i]["Snippets"][
            "Regex_Code"
        ]
        code_snippet_regex_code_list.append(added_snippet_regex)

    return code_snippet_regex_code_list


def no_wl_no_cs_find_target_line(source_code_list, code_snippet_regex_code_list):
    """Method finds target source code lines to scan for no workload, no code snippet use case"""
    faultable_line_list = []
    faultable_line_number_list = []
    len_source_code_list = len(source_code_list)

    for line_number in range(len_source_code_list):
        line = source_code_list[line_number]

        find_function = re.findall("def:*", line)
        find_class = re.findall("class:*", line)
        find_import = re.findall("import", line)
        find_comment = re.findall("#", line)
        if (
            not find_function
            and not find_class
            and not find_import
            and not find_comment
        ):
            for regex_pattern in code_snippet_regex_code_list:
                is_exist = re.findall(regex_pattern, line)
                if is_exist:
                    faultable_line_list.append(line)
                    faultable_line_number_list.append(line_number)

    return faultable_line_number_list, faultable_line_list


# Yes Workload, No Code Snippet
def workload_test_yes_workload_no_snippet(workload_data, split_text):
    """Method is tested workload to use for yes workload, no code snippet use case"""
    painted_lines = []
    painted_lines_number = []
    workload_function_name_list = []

    try:
        for i in range(0, len(workload_data["Tasks"])):
            workload_name_from_json = workload_data["Tasks"][i]["Task"]["Task_ID"]
            search_workload_name_from_json = "def " + workload_name_from_json
            workload_function_name_list.append(search_workload_name_from_json)
    except:
        print("Workload Build Error!")

    for number, line in enumerate(split_text):
        for function_name_from_workload in workload_function_name_list:
            is_function_in_sentence = re.findall(function_name_from_workload, line)
            if is_function_in_sentence:
                while number != 0:
                    leading_spaces = len(split_text[number]) - len(
                        split_text[number].lstrip()
                    )
                    if leading_spaces != 0:
                        painted_lines_number.append(number)
                        painted_lines.append(line)
                        number += 1
                    else:
                        break

    return painted_lines, painted_lines_number


def yes_workload_no_snippet_target_line(patterns, painted_lines, split_text):
    """Find line to use for scan process in yes workload, no code snippet use case"""
    faultable_line_list = []
    faultable_line_number_list = []

    for line_number in painted_lines:
        detected_parts_list_line = split_text[line_number]
        find_function = re.findall("def:*", detected_parts_list_line)
        find_class = re.findall("class:*", detected_parts_list_line)
        find_import = re.findall("import", detected_parts_list_line)
        find_comment = re.findall("#", detected_parts_list_line)
        if (
            not find_function
            and not find_class
            and not find_import
            and not find_comment
        ):
            for pattern in patterns:
                result = re.findall(pattern, detected_parts_list_line, re.MULTILINE)
                if result:
                    faultable_line_list.append(detected_parts_list_line)
                    faultable_line_number_list.append(line_number)

    return faultable_line_list, faultable_line_number_list


# No Workload, Yes Code Snippet
def define_code_snippet_no_workload_yes_code_snippet(code_snippet_data_list):
    """Method defines the code snipppets to use for no workload, yes code snippet use case"""
    patterns = []
    code_snippet_regex_code = open_code_snip()

    added_snippet_regex_length = len(code_snippet_regex_code["code_snippets"])
    for i in range(0, added_snippet_regex_length):
        added_snippet_name = code_snippet_regex_code["code_snippets"][i]["Snippets"][
            "Snippet_Name"
        ]
        added_snippet_regex = code_snippet_regex_code["code_snippets"][i]["Snippets"][
            "Regex_Code"
        ]
        for snippet in code_snippet_data_list:
            if snippet == added_snippet_name:
                patterns.append(added_snippet_regex)
    return patterns


def find_target_no_workload_yes_code_snippet(split_text, patterns):
    """Target code lines are found by IM-FIT to use for no workload, yes code snippet use case"""
    faultable_line_list = []
    faultable_line_number_list = []

    for i, _ in enumerate(split_text):
        line_from_source_code = split_text[i]
        find_function = re.findall("def:*", line_from_source_code)
        find_class = re.findall("class:*", line_from_source_code)
        find_import = re.findall("import", line_from_source_code)
        find_comment = re.findall("#", line_from_source_code)
        if (
            not find_function
            and not find_class
            and not find_import
            and not find_comment
        ):
            for pattern in patterns:
                result = re.findall(pattern, line_from_source_code, re.MULTILINE)
                if result:
                    faultable_line_list.append(line_from_source_code)
                    faultable_line_number_list.append(i)

    return faultable_line_list, faultable_line_number_list
