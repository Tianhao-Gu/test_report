/*
A KBase module: test_report
*/

module test_report {

    typedef structure{
        string workspace_name;
    } Input;

    typedef structure{
        string report_name;
        string report_ref;
    }Result;

    funcdef run_test_report(Input params)
        returns (Result returnVal) authentication required;
};
