# Discovering vulnerabilities in PHP web applications

## Change Logs

- **05Jan2013**: Extends deadline for experimental part to **Monday, 09January2013, 5pm**. The 5 PHP patterns can be submitted until the deadline of the report (in the group repo and with name `5-patterns.json`).
- **28Dec2022**: Adds notes regarding [project report](#project-report).
- **28Dec2022**: Details [mandatory constructs](#precision-and-scope).
- **26Dec2022**: Add info on how to [generate PHP slices](generate_slices.md)
- **26Dec2022**: Add info for the `Common-Tests` repository, and scripts for format validation of patterns and outputs. More info [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/project/common-tests).
- **26Dec2022**: Renamed examples folder to `outputs` to avoid clashes with group's output folder `output`.

## 1\. Aims of this project

- To achieve an in-depth understanding of a security [problem](#2-problem).
- To tackle the problem with a hands-on approach, by implementing a tool.
- To analyse a tool's underlying security mechanism according to the guarantees that it offers, and to its intrinsic limitations.
- To understand how the proposed solution relates to the state of the art of research on the security problem.
- To develop collaboration skills.

### Components

The Project is presented in [Section 2](#2-problem) as a problem, and its solution should have the following two parts:

1. An experimental component, consisting in the development and evaluation of a tool in your language of choice, according to the [Specification of the Tool](#3-specification-of-the-tool).
2. An analysis component, where the strengths and limitations of the tool are critically discussed and presented in a [Report](#4-report).

### Submissions

Important dates and instructions:

- Groups of 3 students should register in Fénix by **17 December 2022**.
- The submission deadline for the **code is 9 January 2023, 16:59**.
  - Please submit your code via your group's private repository (to be created) at GitLab@RNL, under the appropriate Group number `https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/project/project-groups/GroupXX`.
  - The submissions should include all the necessary code and a `README.md` that specifies how the tool should be used.
  - All tests that you would like to be considered for the evaluation of your tool should be made available in a common repository `https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/project/common-tests`. More info [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/project/common-tests).
- The submission deadline for the **report is 13 January 2023, 16:59**. **This also applies to the 5 PHP patterns**.
  - The report should be submitted as a pdf **via Fénix**.
- **Demonstration and a discussion** regarding the tool and report will take place between **16-20 January 2023**.

### Authorship

Projects are to be solved in groups of 3 students. All members of the group are expected to be equally involved in solving, writing and presenting the project, and share full responsibility for all aspects of all components of the evaluation. Presence at the discussion and tool demonstration is mandatory for all group members.

All sources should be adequately cited. [Plagiarism](https://en.wikipedia.org/wiki/Plagiarism) will be punished according to the rules of the School.

## 2\. Problem

A large class of vulnerabilities in applications originates in programs that enable user input information to affect the values of certain parameters of security sensitive functions. In other words, these programs encode a potentially dangerous information flow, in the sense that low integrity -- tainted -- information (user input) may interfere with high integrity parameters of sensitive functions **or variables** (so called sensitive sinks). This means that users are given the power to alter the behavior of sensitive functions **or variables**, and in the worst case may be able to induce the program to perform security violations. For this reason, such flows can be deemed illegal for their potential to encode vulnerabilities.

It is often desirable to accept certain illegal information flows, so we do not want to reject such flows entirely. For instance, it is useful to be able to use the inputted user name for building SQL queries. It is thus necessary to differentiate illegal flows that can be exploited, where a vulnerability exists, from those that are inoffensive and can be deemed secure, or endorsed, where there is no vulnerability. One approach is to only accept programs that properly sanitize the user input, and by so restricting the power of the user to acceptable limits, in effect neutralizing the potential vulnerability.

The aim of this project is to study how web vulnerabilities can be detected statically by means of taint and input sanitization analysis. We choose as a target the PHP language.

The following references are mandatory reading about the problem:

- Yao-Wen Huang et. al., [Securing web application code by static analysis and runtime protection](https://dl.acm.org/doi/10.1145/988672.988679), WWW'04.
- Gary Wassermann and Zhendong Su,  [Sound and Precise Analysis of Web Applications for Injection Vulnerabilities](https://dl.acm.org/doi/10.1145/1250734.1250739), PLDI'07.
- Davide Balzarotti et. al., [Saner: Composing Static and Dynamic Analysis to Validate Sanitization in Web Applications](https://ieeexplore.ieee.org/document/4531166), S&P'08.
- Ibéria Medeiros et. al., [Automatic Detection and Correction of Web Application Vulnerabilities using Data Mining to Predict False Positives](https://dl.acm.org/doi/10.1145/2566486.2568024), WWW'14.

## 3\. Specification of the Tool

The experimental part consists in the development of a static analysis tool for identifying data and information flow violations that are not protected in the program.

Static analysis is a general term for techniques that verify the behavior of applications by inspecting their code (typically their source code). Static analysis tools are complex so, and in order to focus on the flow analysis, **the aim is not to implement a complete tool**. Instead, it will be assumed that the code to be analyzed has undergone a pre-processing stage to isolate, in the form of a _program slice_, a sequence of PHP instructions that are considered to be relevant to our analysis.

The following code slice, which is written in PHP, contains code lines which may impact a data flow between a certain entry point and a sensitive sink. The variables `$u` and `$p` are the values of the request parameters and are given by the user. These variables are then concatenated in a string that is passed to the `mysql_query()` method, which executes the given database operation query.

    $u = $_GET['username'];
    $p = $_GET['password'];
    $q = "SELECT * FROM users WHERE user='" . $u . "' AND password='" . $p . "'";
    $query = mysql_query($q);

Inspecting this slice it is clear that the program from which the slice was extracted can potentially encode a SQL injection vulnerability. An attacker can inject a malicious username like `' OR 1 = 1 --`, modifying the structure of the query and this way bypassing the password validation.

The aim of the tool is to search the slices for vulnerabilities according to inputted patterns, which specify for a given type of vulnerability its possible sources (a.k.a. entry points), sanitizers and sinks. A _pattern_ is thus a 5-tuple with:

- name of vulnerability (e.g., SQL injection)
- a set of entry points (e.g., `$_GET`),
- a set of sanitization functions (e.g., `mysql_real_escape_string`),
- a set of sensitive sinks (e.g., `mysql_query`),
- and a flag indicating whether implicit flows are to be considered.

The tool should signal potential vulnerabilities and sanitization efforts: if it identifies a possible data flow from an entry point to a sensitive sink (according to the inputted patterns), it should report a potential vulnerability; if the data flow passes through a sanitization function, _it should still report the vulnerability_, but also acknowledge the fact that its sanitization is possibly being addressed.

We provide program slices and patterns to assist you in testing the tool. It is however each group's responsibility to perform more extensive testing for ensuring the correctness and robustness of the tool. Note however that for the purpose of testing, the names of vulnerabilities, sources, sanitizers and sinks are irrelevant and do not need to be real vulnerabilities. In this context, you can produce your own patterns without specific knowledge of vulnerabilities, as this will not affect the ability of the tool to manage meaningful patterns. See examples in Section [Input Vulnerability Patterns](#input-vulnerability-patterns)

### Running the tool

The tool should be called in the command line. All input and output should be encoded in [JSON](http://www.json.org/), according to the specifications that follow.

Your program should receive two arguments, which are the only input that it should consider:

- the name of the JSON file containing the program slice to analyse, represented in the form of an Abstract Syntax Tree;
- the name of the JSON file containing the list of vulnerability patterns to consider.

You can assume that the parsing of the PHP slices has been done, and that the input files are [well-formed](#input-program-slices). The analysis should be fully customizable to the inputted [vulnerability patterns](#input-vulnerability-patterns) described below. In addition to the entry points specified in the patterns, **by default any non-instantiated variable that appears in the slice is to be considered as an entry point to all vulnerabilities being considered**.

The output should list the potential vulnerabilities encoded in the slice, and an indication of which instruction(s) (if any) have been applied. The format of the output is specified [below](#output).

_NOTE: Scripts to generate correct inputs, and that validate the correct format of the pattern and output files will be made available during the first week of the project._

The way to call your tool depends on the language in which you choose to implement it, but it should:

1. be called in the command line with two arguments `<slice>.json` and  `<patterns>.json`
2. produce the output referred below and no other to a file named `<slice>.output.json`
3. the output file should be created in the `./output/` folder.

For example

    $ ./php-analyser slice.json patterns.json
    
    $ python ./php-analyser.py slice.json patterns.json
    
    $ java php-analyser slice.json patterns.json

You are free to choose the programming language for the implementation, as long as your tool is runnable in the labs or VM (in case of doubt please ask).

### Input. Program slices

Your program should read from a text file (given as first argument in the command line) the representation of a PHP slice in the form of an Abstract Syntax Tree (AST). The AST is represented in JSON, using the same structure as in [PHP Parser library](https://github.com/nikic/PHP-Parser).

For instance, the slice

    echo '<p>Hello World</p>'; 

is represented as

    [
        {
            "nodeType": "Stmt_Echo",
            "attributes": {
                "startLine": 2,
                "endLine": 2
            },
            "exprs": [
                {
                    "nodeType": "Scalar_String",
                    "attributes": {
                        "startLine": 2,
                        "endLine": 2,
                        "kind": 1,
                        "rawValue": "'<p>Hello World<\/p>'"
                    },
                    "value": "<p>Hello World<\/p>"
                }
            ]
        }
    ]

and the slice

    $u = $_GET['username'];
    $p = $_GET['password'];
    $q = "SELECT * FROM users WHERE user='" . $u . "' AND password='" . $p . "'";
    $query = mysql_query($q);

is represented as:

    [
        {
            "nodeType": "Stmt_Expression",
            "attributes": {
                "startLine": 2,
                "endLine": 2
            },
            "expr": {
                "nodeType": "Expr_Assign",
                "attributes": {
                    "startLine": 2,
                    "endLine": 2
                },
                "var": {
                    "nodeType": "Expr_Variable",
                    "attributes": {
                        "startLine": 2,
                        "endLine": 2
                    },
                    "name": "u"
                },
                "expr": {
                    "nodeType": "Expr_ArrayDimFetch",
                    "attributes": {
                        "startLine": 2,
                        "endLine": 2
                    },
                    "var": {
                        "nodeType": "Expr_Variable",
                        "attributes": {
                            "startLine": 2,
                            "endLine": 2
                        },
                        "name": "_GET"
                    },
                    "dim": {
                        "nodeType": "Scalar_String",
                        "attributes": {
                            "startLine": 2,
                            "endLine": 2,
                            "kind": 1,
                            "rawValue": "'username'"
                        },
                        "value": "username"
                    }
                }
            }
        },
        {
            "nodeType": "Stmt_Expression",
            "attributes": {
                "startLine": 3,
                "endLine": 3
            },
            "expr": {
                "nodeType": "Expr_Assign",
                "attributes": {
                    "startLine": 3,
                    "endLine": 3
                },
                "var": {
                    "nodeType": "Expr_Variable",
                    "attributes": {
                        "startLine": 3,
                        "endLine": 3
                    },
                    "name": "q"
                },
                "expr": {
                    "nodeType": "Expr_BinaryOp_Concat",
                    "attributes": {
                        "startLine": 3,
                        "endLine": 3
                    },
                    "left": {
                        "nodeType": "Expr_BinaryOp_Concat",
                        "attributes": {
                            "startLine": 3,
                            "endLine": 3
                        },
                        "left": {
                            "nodeType": "Expr_BinaryOp_Concat",
                            "attributes": {
                                "startLine": 3,
                                "endLine": 3
                            },
                            "left": {
                                "nodeType": "Expr_BinaryOp_Concat",
                                "attributes": {
                                    "startLine": 3,
                                    "endLine": 3
                                },
                                "left": {
                                    "nodeType": "Scalar_String",
                                    "attributes": {
                                        "startLine": 3,
                                        "endLine": 3,
                                        "kind": 2,
                                        "rawValue": "\"SELECT * FROM users WHERE user='\""
                                    },
                                    "value": "SELECT * FROM users WHERE user='"
                                },
                                "right": {
                                    "nodeType": "Expr_Variable",
                                    "attributes": {
                                        "startLine": 3,
                                        "endLine": 3
                                    },
                                    "name": "u"
                                }
                            },
                            "right": {
                                "nodeType": "Scalar_String",
                                "attributes": {
                                    "startLine": 3,
                                    "endLine": 3,
                                    "kind": 2,
                                    "rawValue": "\"' AND password='\""
                                },
                                "value": "' AND password='"
                            }
                        },
                        "right": {
                            "nodeType": "Expr_Variable",
                            "attributes": {
                                "startLine": 3,
                                "endLine": 3
                            },
                            "name": "p"
                        }
                    },
                    "right": {
                        "nodeType": "Scalar_String",
                        "attributes": {
                            "startLine": 3,
                            "endLine": 3,
                            "kind": 2,
                            "rawValue": "\"'\""
                        },
                        "value": "'"
                    }
                }
            }
        },
        {
            "nodeType": "Stmt_Expression",
            "attributes": {
                "startLine": 4,
                "endLine": 4
            },
            "expr": {
                "nodeType": "Expr_Assign",
                "attributes": {
                    "startLine": 4,
                    "endLine": 4
                },
                "var": {
                    "nodeType": "Expr_Variable",
                    "attributes": {
                        "startLine": 4,
                        "endLine": 4
                    },
                    "name": "query"
                },
                "expr": {
                    "nodeType": "Expr_FuncCall",
                    "attributes": {
                        "startLine": 4,
                        "endLine": 4
                    },
                    "name": {
                        "nodeType": "Name",
                        "attributes": {
                            "startLine": 4,
                            "endLine": 4
                        },
                        "parts": [
                            "mysql_query"
                        ]
                    },
                    "args": [
                        {
                            "nodeType": "Arg",
                            "attributes": {
                                "startLine": 4,
                                "endLine": 4
                            },
                            "name": null,
                            "value": {
                                "nodeType": "Expr_Variable",
                                "attributes": {
                                    "startLine": 4,
                                    "endLine": 4
                                },
                                "name": "q"
                            },
                            "byRef": false,
                            "unpack": false
                        }
                    ]
                }
            }
        }
    ]

In order to parse the ASTs, you can use an off-the-shelf parser for JSON or build your own. Note that not all of the information that is available in the AST needs necessarily to be used and stored by your program.

Besides the slices that are made available, you can produce your own ASTs for testing your program by using the provided parser [slice-parser.php](slice-parser.php). You can visualize the JSON outputs as a tree using [this online tool](http://jsonviewer.stack.hu/).

### Input. Vulnerability patterns

The patterns are to be loaded from a file, whose name is given as the second argument in the command line. You can assume that pattern names are unique.

An example JSON file with four patterns:

    [
        {
            "vulnerability": "SQL injection 1",
            "sources": ["$_GET", "$_POST", "$_COOKIE"],
            "sanitizers": ["mysql_escape_string", "mysql_real_escape_string"],
            "sinks": ["mysql_query", "mysql_unbuffered_query","mysql_db_query"],
            "implicit": "no"
        },
        {
            "vulnerability": "SQL injection 2",
            "sources": ["$_GET", "$_POST", "$_COOKIE""],
            "sanitizers": ["pg_escape_string", "pg_escape_bytea"],
            "sinks": ["pg_query", "pg_send_query"],
            "implicit": "yes"
        },
        {
            "vulnerability": "XSS 1",
            "sources": ["$_GET", "$_POST", "$_COOKIE"],
            "sanitizers": ["htmlspecialchars"],
            "sinks": ["echo", "print"],
            "implicit": "no"
        },
        {
            "vulnerability": "Private Vulnerability",
            "sources": ["r"],
            "sanitizers": ["f"],
            "sinks": ["$g", "h"],
            "implicit": "yes"
        }
    ]

### Output

The output of the program is a `JSON` list of vulnerability objects that should be written to a file `./output/<slice>.output.json` where `<slice>.json` is the program slice under analysis. The structure of the objects should include 5 pairs, with the following meaning:

- `vulnerability`: name of vulnerability (string, according to inputted pattern)
- `source`: input source (string, according to inputted pattern)
- `sink`: sensitive sink (string, according to inputted pattern)
- `unsanitized flows`: whether there are unsanitized flows (string)
- `sanitized flows`: sanitizing functions if present, otherwise empty (list of lists of strings)

As an example, the output with respect to the program and patters that appear in the examples in [Specification of the Tool](#3-specification-of-the-tool) would be:

    [
        {
            "vulnerability": "SQL injection 1",
            "source": "$_GET",
            "sink": "mysql_query",
            "unsanitized flows": "yes",
            "sanitized flows": []
        }
    ]

The output list must include a vulnerability object for every pair source-sink between which there is at least one flow of information. If at least one of the flows is not sanitized, it must be signaled. Since it is possible that there are more than one flow paths for a given pair source-sink, that could be sanitized in different ways, sanitized flows are represented as a list. Since each flow might be sanitized by more than one sanitizer, each flow is itself a list **(with no particular order)**.

More precisely, the format of the output should be:

    <OUTPUT> ::= [ <VULNERABILITIES> ]
    <VULNERABILITIES> := "none" | <VULNERABILITY> | <VULNERABILITY>,<VULNERABILITIES>
    <VULNERABILITY> ::= { "vulnerability":"<STRING>",
                        "source":"<STRING>",
                        "sink":"<STRING>",
                        "unsanitized flows": <YESNO>,
                        "sanitized flows": [ <FLOWS> ] }
    <YESNO> ::= "yes" | "no"
    <FLOWS> ::= "none" | <FLOW> | <FLOW>,<FLOWS>
    <FLOW> ::= [ <SANITIZERS> ]
    <SANITIZERS> ::= <STRING> | <STRING>,<SANITIZERS>

_Note_: A flow is said to be sanitized if it goes "through" an appropriate sanitizer, i.e., if at some point the entire information is converted into the output of a sanitizer.

### Precision and scope

The security property that underlies this project is the following:

_Given a set of vulnerability patterns of the form (vulnerability name, a set of entry points, a set of sensitive sinks, a set of sanitizing functions), a program is secure if it does not encode, for any given vulnerability pattern, an information flow from an entry point to a sensitive sink, unless the information goes through a sanitizing function._

You will have to make decisions regarding whether your tool will signal, or not, illegal taint flows that are encoded by certain combinations of program constructs. You can opt for an approach that simplifies the analysis. This simplification may introduce or omit features that could influence the outcome, thus leading to wrong results.

Note that the following criteria will be valued:

- _Soundness_ - successful detection of illegal taint flows (i.e., true positives). In particular, treatment of implicit taint flows will be valued.
- _Precision_ - avoiding signalling programs that do not encode illegal taint flows (i.e., false-positives). In particular, sensitivity to the order of execution will be valued.
- Scope - treatment of a larger subset of the language. The mandatory language constructs are those that appear in the slices provided, and include: assignments, binary operations, function calls, condition test and while loop.

Using the same terms as in [PHP Parser](https://github.com/nikic/PHP-Parser/tree/4.x/lib/PhpParser/Node) the mandatory constructs are those associated with nodes of type

- Literals/Scalars (DNumber, LNumber, String), Constants (ConstFetch), and Variables
- Expressions
  - Ops: BinaryOp, BitwiseNot, BooleanNot
  - Assignments: Assign, AssignOp, Post/Pre-Dec/Inc
  - FuncCall
  - ArrayDimFetch (only for reading, and assume in this case that index is always by a constant and the name of the array is the eventually tainted expression, eg, $_GET['username'])
- Statements
  - Expression
  - If/Else
  - While
  - Echo
  - Break, Continue

When designing and implementing this component, you are expected to take into account and to incorporate precision and efficiency considerations, as discussed in the critical analysis criteria for the report.

## 4\. Report

### Critical Analysis

Consider the security property expressed in [Precision and scope](#precision-and-scope), and the security mechanism that is studied in this project, which comprises:

- A component (assume already available) that statically extracts the program slices that could encode potential vulnerabilities in a program.
- A tool (developed by you), that receives a configuration file containing vulnerability patterns, and signals potential vulnerabilities in given slices according to those patterns, as well as possible sanitization efforts, as implemented by you in the experimental part.

Given the intrinsic limitations of the static analysis problem, the developed tool is necessarily imprecise in determining which programs encode vulnerabilities or not. It can be unsound (produce false negatives), incomplete (produce false positives), or both.

1. Explain and give examples of what are the imprecisions that are built into the proposed mechanism. Have in mind that they can originate at different levels:
    - imprecise tracking of information flows
        - Are all illegal information flows captured by the adopted technique? (false negatives)
        - Are there flows that are unduly reported? (false positives)
    - imprecise endorsement of input sanitization
        - Are there sanitization functions that could be ill-used and do not properly sanitize the input? (false negatives)
        - Are all possible sanitization procedures detected by the tool? (false positives)
    - **Make sure that you give at least one example to the 4 questions above.**
2. _For each_ of the identified imprecisions that lead to:
    - undetected vulnerabilities (false negatives)
        - Can these vulnerabilities be exploited?
        - If yes, how (give concrete examples)?
    - reporting non-vulnerabilities (false positives)
        - Can you think of how they could be avoided?
    - **Make sure that you answer these questions at least for each of the 4 examples given above.**.
3. Propose one way of making the tool more precise, and predict what would be the trade-offs (efficiency, precision) involved in this change. You can use the papers suggested above for ideas of other techniques that could be used.

### Structure

Report your work and your conclusions in a written document, using no more than 4 pages, single column, (excluding references and appendices), according to the following guidelines:

- Use a structure that helps to read and find the relevant information. **Whenever possible, use tables and pseudo-code to structure this information**.
- Assume a reader acquainted with the context of the Project (in other words go precisely and straight to the point!).
- Briefly describe the experimental part, presenting the architecture of the tool and the main design options.
- Define and discuss what your tool is able to achieve, making sure that you answer all the questions mentioned above in [Critical Analysis](#critical-analysis).

We suggest that your report follows the structure below and each section addresses the presented questions:

1. Introduction: introduce the context of your work (1 paragraph)
    - _What is the problem that you want to solve? Why is it important?_
2. Usage: demonstrate the behavior of the tool (1 paragraph)
    - _How do you use the tool? What does it do?_
3. Implementation: explain the approach and the underlying techniques behind the tool (1 page, possible diagram, max 1 paragraph per each item below)
    - _What data structures did you use to internally represent the AST? (data types and names of relevant variables and classes)_
    - _What are the security classes used by your analysis? (specify what information they contain)_
    - _How is the AST traversed? (specify the order and say which functions perform it. Present it ideally as an algorithm in pseudo-code)_
    - _How are basic vulnerabilities detected? (relate it to the traversal algorithm)_
    - _How (and if) are implicit vulnerabilities detected? (relate it to the traversal algorithm)_
4. Test and Evaluate: explain how did you test the correctness and robustness of your tool. In particular
    - _which tests did you perform?_
    - _what is the rationale for each test?_
5. Critical Analysis: identify the strengths and limitations of the tool in a structured form (1-2 pages)
    - Identification of imprecisions: present a table that answers (yes/no) to each of the 4 questions identified in item 1 of [Section Critical Analysis](#critical-analysis) above (false positives/false negatives of imprecise tracking/imprecise endorsement).
        - **In case of an affirmative answer, provide a snippet of code that illustrates it**.
    - Understanding of imprecisions: Can the identified false negatives lead to exploits?
        - **Provide the sequence of steps, or justify why it is not possible**.
    - Understanding of imprecisions: Can the identified false positives be improved?
        - **Briefly describe how these improvements could be done**.
    - Improving precision: What other program analysis techniques could be incorporated into your tool in order to improve precision?
        - _Discuss how it could help_.
6. Related work: discuss how existing work relates to yours (2-3 paragraphs)
    - What other tools address the same problem for the considered language? Discuss similarities and differences.
    - What other tools use the same technique for solving similar problems?
    - **Make sure that you refer at least to the 4 papers given above, and try to include 2 other that you find via these papers' references or via eg. Google Scholar.**
7. Conclusion: what are your tool's main achievements? (1 paragraph)
    - What is your tool good for?
    - What could you improve in your tool?

## 5\. Grading

### Discussion

The baseline grade for the group will be determined based on the experimental part and report, according to the rules below. During the discussion, all students in the group are expected to be able to demonstrate knowledge of all details of these two components. In order to be graded for the project, each student must participate in the discussion, and his/her grade might be adjusted accordingly.

### Experimental part

Grading of the Tool and Patterns will reflect the level of complexity of the developed tool, according to the following:

- Basic vulnerability detection (50%) - signals potential vulnerability based solely on explicit flows in slices with mandatory constructs
- Advanced vulnerability detection (25%) - signals potential vulnerability that can include implicit flows in slices with mandatory constructs
- Sanitization recognition (15%) - signals potential sanitization of vulnerabilities
- Definition of a minimum of 5 appropriate PHP Vulnerability Patterns (5%) - consider the provided and other related work. To be submitted in the same repo as the Group's project under name `5-patterns.json`.
- Distinguish patterns vulnerability data (5%) - respects which sources correspond to which sinks for different vulnerabilities, and which functions may sanitize which vulnerabilities
- Bonus (5%) - treats other program constructs beyond the mandatory ones, extra effort for avoiding false positives

This part corresponds to 2/3 of the project grade.

### Report

The maximum grade of the report does not depend on the complexity of the tool. It will of course reflect whether the analysis of the imprecisions matches the precision of the tool that was developed (which in turn depends on the complexity of the tool). The components of the grading are worth 20% each, and are the following:

- Quality of writing - structure of the report, clarity of the ideas
- Related work - depth of understanding of the related work, detachment from words used in cited papers. See mandatory references in [Problem](#2-problem) above.
- Identification of imprecisions - connection with experimental work. See question 1 in [Section Critical Analysis](#critical-analysis) above.
- Understanding of imprecisions - connection with experimental work. See question 2 in [Section Critical Analysis](#critical-analysis) above.
- Improving precision - originality, own ideas. See question 3 in [Section Critical Analysis](#critical-analysis) above.
- Bonus (10%) - cites other references beyond the mandatory ones. See references in [Problem](#2-problem) above.

This part corresponds to 1/3 of the project grade.

## 6\. Other Materials

For each slice `slice.php` we provide the AST `slice.json`, a pattern `slice.patterns.json`, and the expected output `slice.output.json` according to these vulnerability patterns.

- [Slices](slices/)
- [ASTs](slices_ast/)
- [Patterns](patterns/)
- [Outputs](outputs/)
