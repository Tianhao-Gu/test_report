# -*- coding: utf-8 -*-
#BEGIN_HEADER
import uuid
import os

from KBaseReport.KBaseReportClient import KBaseReport
#END_HEADER


class test_report:
    '''
    Module Name:
    test_report

    Module Description:
    A KBase module: test_report
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass

    def run_test_report(self, ctx, params):
        """
        :param params: instance of type "Input" -> structure: parameter
           "workspace_name" of String
        :returns: instance of type "Result" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_test_report
        report_params = {'message': 'this is a report message',
                         'workspace_name': params.get('workspace_name'),
                         # 'objects_created': objects_created,
                         # 'file_links': output_files,
                         # 'html_links': output_html_files,
                         # 'direct_html_link_index': 0,
                         # 'html_window_height': 333,
                         'report_object_name': 'kb_test_report_' + str(uuid.uuid4())}

        kbase_report_client = KBaseReport(os.environ['SDK_CALLBACK_URL'])
        output = kbase_report_client.create_extended_report(report_params)

        returnVal = {'report_name': output['name'], 'report_ref': output['ref']}

        #END run_test_report

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_test_report return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
