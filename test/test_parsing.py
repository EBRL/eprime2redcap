#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'

import os
import unittest

import ep2rc

wd = os.path.split(__file__)[0]
print wd

def parse(f):
    with open(f) as fo:
        data = ep2rc.parse_file(f, fo)
    return data

class NFTests(unittest.TestCase):
    """ NF Testing """
    
    def test_MI(self):
        f = os.path.join(wd, 'NF_MI_Test_Test_Pre.txt')
        correct = {'grant': 'NF',
                    'id': 'Test_Test',
					'mi1_pre_m1_cont_acc': '100.000',
					'mi1_pre_m1_cont_accsd': '0.000',
					'mi1_pre_m1_cont_fn': '0',
					'mi1_pre_m1_cont_fp': '0',
					'mi1_pre_m1_cont_omit': '0',
					'mi1_pre_m1_cont_rtavg': '823.292',
					'mi1_pre_m1_cont_rtsd': '98.016',
					'mi1_pre_m1_imag_acc': '100.000',
					'mi1_pre_m1_imag_accsd': '0.000',
					'mi1_pre_m1_imag_fn': '0',
					'mi1_pre_m1_imag_fp': '0',
					'mi1_pre_m1_imag_omit': '0',
					'mi1_pre_m1_imag_rtavg': '995.208',
					'mi1_pre_m1_imag_rtsd': '222.342',
					'mi1_pre_m2_cont_acc': '100.000',
					'mi1_pre_m2_cont_accsd': '0.000',
					'mi1_pre_m2_cont_fn': '0',
					'mi1_pre_m2_cont_fp': '0',
					'mi1_pre_m2_cont_omit': '0',
					'mi1_pre_m2_cont_rtavg': '804.917',
					'mi1_pre_m2_cont_rtsd': '79.943',
					'mi1_pre_m2_imag_acc': '91.667',
					'mi1_pre_m2_imag_accsd': '0.276',
					'mi1_pre_m2_imag_fn': '0',
					'mi1_pre_m2_imag_fp': '2',
					'mi1_pre_m2_imag_omit': '0',
					'mi1_pre_m2_imag_rtavg': '967.227',
					'mi1_pre_m2_imag_rtsd': '187.644',
					'mi1_pre_upload': 'yes'}
        data = parse(f)        
        self.assertEqual(data, correct, "Failed parsing NF MI")
        
    def test_SWR(self):
        f = os.path.join(wd, 'NF_SWR_Test_Test_Pre_ListA.txt')
        correct = {'grant': 'NF',
                    'id': 'Test_Test',
					'swr1_pre_m1_hai_acc': '100.000',
					'swr1_pre_m1_hai_accsd': '0.000',
					'swr1_pre_m1_hai_comit': '0',
					'swr1_pre_m1_hai_omit': '0',
					'swr1_pre_m1_hai_rtavg': '903.500',
					'swr1_pre_m1_hai_rtsd': '203.129',
					'swr1_pre_m1_har_acc': '90.000',
					'swr1_pre_m1_har_accsd': '0.300',
					'swr1_pre_m1_har_comit': '0',
					'swr1_pre_m1_har_omit': '1',
					'swr1_pre_m1_har_rtavg': '834.000',
					'swr1_pre_m1_har_rtsd': '181.275',
					'swr1_pre_m1_hci_acc': '80.000',
					'swr1_pre_m1_hci_accsd': '0.400',
					'swr1_pre_m1_hci_comit': '1',
					'swr1_pre_m1_hci_omit': '1',
					'swr1_pre_m1_hci_rtavg': '1008.000',
					'swr1_pre_m1_hci_rtsd': '234.094',
					'swr1_pre_m1_hcr_acc': '80.000',
					'swr1_pre_m1_hcr_accsd': '0.400',
					'swr1_pre_m1_hcr_comit': '1',
					'swr1_pre_m1_hcr_omit': '1',
					'swr1_pre_m1_hcr_rtavg': '905.500',
					'swr1_pre_m1_hcr_rtsd': '252.108',
					'swr1_pre_m1_nonword_acc': '50.000',
					'swr1_pre_m1_nonword_accsd': '0.500',
					'swr1_pre_m1_nonword_comit': '1',
					'swr1_pre_m1_nonword_omit': '4',
					'swr1_pre_m1_nonword_rtavg': '1153.000',
					'swr1_pre_m1_nonword_rtsd': '159.087',
					'swr1_pre_m1_word_acc': '87.500',
					'swr1_pre_m1_word_accsd': '0.331',
					'swr1_pre_m1_word_comit': '2',
					'swr1_pre_m1_word_omit': '3',
					'swr1_pre_m1_word_rtavg': '909.971',
					'swr1_pre_m1_word_rtsd': '225.808',
					'swr1_pre_m2_hai_acc': '50.000',
					'swr1_pre_m2_hai_accsd': '0.500',
					'swr1_pre_m2_hai_comit': '3',
					'swr1_pre_m2_hai_omit': '2',
					'swr1_pre_m2_hai_rtavg': '886.800',
					'swr1_pre_m2_hai_rtsd': '181.495',
					'swr1_pre_m2_har_acc': '50.000',
					'swr1_pre_m2_har_accsd': '0.500',
					'swr1_pre_m2_har_comit': '3',
					'swr1_pre_m2_har_omit': '2',
					'swr1_pre_m2_har_rtavg': '934.600',
					'swr1_pre_m2_har_rtsd': '245.122',
					'swr1_pre_m2_hci_acc': '60.000',
					'swr1_pre_m2_hci_accsd': '0.490',
					'swr1_pre_m2_hci_comit': '2',
					'swr1_pre_m2_hci_omit': '2',
					'swr1_pre_m2_hci_rtavg': '861.667',
					'swr1_pre_m2_hci_rtsd': '178.815',
					'swr1_pre_m2_hcr_acc': '60.000',
					'swr1_pre_m2_hcr_accsd': '0.490',
					'swr1_pre_m2_hcr_comit': '0',
					'swr1_pre_m2_hcr_omit': '4',
					'swr1_pre_m2_hcr_rtavg': '822.167',
					'swr1_pre_m2_hcr_rtsd': '255.906',
					'swr1_pre_m2_nonword_acc': '30.000',
					'swr1_pre_m2_nonword_accsd': '0.458',
					'swr1_pre_m2_nonword_comit': '3',
					'swr1_pre_m2_nonword_omit': '4',
					'swr1_pre_m2_nonword_rtavg': '1139.333',
					'swr1_pre_m2_nonword_rtsd': '226.863',
					'swr1_pre_m2_word_acc': '55.000',
					'swr1_pre_m2_word_accsd': '0.497',
					'swr1_pre_m2_word_comit': '8',
					'swr1_pre_m2_word_omit': '10',
					'swr1_pre_m2_word_rtavg': '873.182',
					'swr1_pre_m2_word_rtsd': '222.190',
					'swr1_pre_upload': 'yes'}
        data = parse(f)        
        self.assertEqual(data, correct, "Failed parsing NF SWR")
    
    def test_PIC(self):
        f = os.path.join(wd, 'NF_PIC_Test_Test_Post_ListA.txt')
        correct = {'grant': 'NF',
                    'id': 'Test_Test',
					'pic1_post_m1_con_acc': '75.000',
					'pic1_post_m1_con_accsd': '0.433',
					'pic1_post_m1_con_comit': '1',
					'pic1_post_m1_con_omit': '4',
					'pic1_post_m1_con_rtavg': '914.533',
					'pic1_post_m1_con_rtsd': '258.595',
					'pic1_post_m1_match_acc': '80.000',
					'pic1_post_m1_match_accsd': '0.400',
					'pic1_post_m1_match_comit': '2',
					'pic1_post_m1_match_omit': '1',
					'pic1_post_m1_match_rtavg': '918.667',
					'pic1_post_m1_match_rtsd': '180.152',
					'pic1_post_m1_psw_acc': '80.000',
					'pic1_post_m1_psw_accsd': '0.400',
					'pic1_post_m1_psw_comit': '0',
					'pic1_post_m1_psw_omit': '4',
					'pic1_post_m1_psw_rtavg': '841.938',
					'pic1_post_m1_psw_rtsd': '217.583',
					'pic1_post_m1_wrd_acc': '90.000',
					'pic1_post_m1_wrd_accsd': '0.300',
					'pic1_post_m1_wrd_comit': '0',
					'pic1_post_m1_wrd_omit': '2',
					'pic1_post_m1_wrd_rtavg': '1035.444',
					'pic1_post_m1_wrd_rtsd': '308.208',
					'pic1_post_m2_con_acc': '80.000',
					'pic1_post_m2_con_accsd': '0.400',
					'pic1_post_m2_con_comit': '0',
					'pic1_post_m2_con_omit': '4',
					'pic1_post_m2_con_rtavg': '864.375',
					'pic1_post_m2_con_rtsd': '252.876',
					'pic1_post_m2_match_acc': '60.000',
					'pic1_post_m2_match_accsd': '0.490',
					'pic1_post_m2_match_comit': '1',
					'pic1_post_m2_match_omit': '5',
					'pic1_post_m2_match_rtavg': '1032.667',
					'pic1_post_m2_match_rtsd': '308.971',
					'pic1_post_m2_psw_acc': '75.000',
					'pic1_post_m2_psw_accsd': '0.433',
					'pic1_post_m2_psw_comit': '1',
					'pic1_post_m2_psw_omit': '4',
					'pic1_post_m2_psw_rtavg': '944.467',
					'pic1_post_m2_psw_rtsd': '245.483',
					'pic1_post_m2_wrd_acc': '70.000',
					'pic1_post_m2_wrd_accsd': '0.458',
					'pic1_post_m2_wrd_comit': '1',
					'pic1_post_m2_wrd_omit': '5',
					'pic1_post_m2_wrd_rtavg': '1032.286',
					'pic1_post_m2_wrd_rtsd': '268.392',
					'pic1_post_upload': 'yes'}
        data = parse(f)        
        self.assertEqual(data, correct, "Failed parsing NF PIC")
    
    def test_REP(self):
        f = os.path.join(wd, 'NF_REP_Test_Test.txt')
        correct = {'grant': 'NF',
                    'id': 'Test_Test',
					'rep1_m1_abs_acc': '93.333',
					'rep1_m1_abs_accsd': '0.249',
					'rep1_m1_abs_comit': '0',
					'rep1_m1_abs_omit': '1',
					'rep1_m1_abs_rtavg': '658.214',
					'rep1_m1_abs_rtsd': '55.606',
					'rep1_m1_conc_acc': '100.000',
					'rep1_m1_conc_accsd': '0.000',
					'rep1_m1_conc_comit': '0',
					'rep1_m1_conc_omit': '0',
					'rep1_m1_conc_rtavg': '684.143',
					'rep1_m1_conc_rtsd': '147.144',
					'rep1_m1_cons_acc': '94.444',
					'rep1_m1_cons_accsd': '0.229',
					'rep1_m1_cons_comit': '1',
					'rep1_m1_cons_omit': '0',
					'rep1_m1_cons_rtavg': '726.765',
					'rep1_m1_cons_rtsd': '149.180',
					'rep1_m1_non_acc': '94.444',
					'rep1_m1_non_accsd': '0.229',
					'rep1_m1_non_comit': '1',
					'rep1_m1_non_omit': '0',
					'rep1_m1_non_rtavg': '823.176',
					'rep1_m1_non_rtsd': '145.454',
					'rep1_m2_abs_acc': '100.000',
					'rep1_m2_abs_accsd': '0.000',
					'rep1_m2_abs_comit': '0',
					'rep1_m2_abs_omit': '0',
					'rep1_m2_abs_rtavg': '715.600',
					'rep1_m2_abs_rtsd': '121.372',
					'rep1_m2_conc_acc': '95.238',
					'rep1_m2_conc_accsd': '0.213',
					'rep1_m2_conc_comit': '0',
					'rep1_m2_conc_omit': '1',
					'rep1_m2_conc_rtavg': '653.150',
					'rep1_m2_conc_rtsd': '131.113',
					'rep1_m2_cons_acc': '100.000',
					'rep1_m2_cons_accsd': '0.000',
					'rep1_m2_cons_comit': '0',
					'rep1_m2_cons_omit': '0',
					'rep1_m2_cons_rtavg': '674.667',
					'rep1_m2_cons_rtsd': '149.149',
					'rep1_m2_non_acc': '100.000',
					'rep1_m2_non_accsd': '0.000',
					'rep1_m2_non_comit': '0',
					'rep1_m2_non_omit': '0',
					'rep1_m2_non_rtavg': '822.389',
					'rep1_m2_non_rtsd': '168.545',
					'rep1_m3_abs_acc': '86.667',
					'rep1_m3_abs_accsd': '0.340',
					'rep1_m3_abs_comit': '0',
					'rep1_m3_abs_omit': '2',
					'rep1_m3_abs_rtavg': '706.769',
					'rep1_m3_abs_rtsd': '164.446',
					'rep1_m3_conc_acc': '100.000',
					'rep1_m3_conc_accsd': '0.000',
					'rep1_m3_conc_comit': '0',
					'rep1_m3_conc_omit': '0',
					'rep1_m3_conc_rtavg': '689.048',
					'rep1_m3_conc_rtsd': '89.770',
					'rep1_m3_cons_acc': '100.000',
					'rep1_m3_cons_accsd': '0.000',
					'rep1_m3_cons_comit': '0',
					'rep1_m3_cons_omit': '0',
					'rep1_m3_cons_rtavg': '697.722',
					'rep1_m3_cons_rtsd': '126.603',
					'rep1_m3_non_acc': '100.000',
					'rep1_m3_non_accsd': '0.000',
					'rep1_m3_non_comit': '0',
					'rep1_m3_non_omit': '0',
					'rep1_m3_non_rtavg': '786.444',
					'rep1_m3_non_rtsd': '130.138',
					'rep1_upload': 'yes'}
        data = parse(f)        
        self.assertEqual(data, correct, "Failed parsing NF REP")


class NFBTests(unittest.TestCase):
    """ NFB Parsing """

    def test_FIG(self):
        f = os.path.join(wd, 'NFB_FIG_212_000000_Pre.txt')
        correct = {'mrt1bmrt': '3607.700',
                    'mrt1bsdrt': '3181.371',
                    'mrt1btc': '9',
                    'mrt1btcp': '45.000',
                    'studyid': '212'}
        data = parse(f)        
        self.assertEqual(data, correct, "Failed parsing NFB FIG")
        
    def test_MI(self):
        f = os.path.join(wd, 'NFB_MI_212_000000_Pre.txt')
        correct = {'mit1mrt': '1701.600',
                    'mit1sdrt': '809.910',
                    'mit1tc': '39',
                    'mit1tcp': '78.000',
                    'mit1tt': '2',
                    'studyid': '212'}
        data = parse(f)
        self.assertEqual(data, correct, "Failed parsing NFB MI")
        
    def test_OLSON(self):
        f = os.path.join(wd, 'NFB_OLSON_212_000000_Pre.txt')
        correct = {'ot1cmrt': '1773.650',
                    'ot1csdrt': '1409.268',
                    'ot1imrt': '1773.650',
                    'ot1isdrt': '1409.268',
                    'ot1tc': '20',
                    'studyid': '212'}
        data = parse(f)
        self.assertEqual(data, correct, "Failed parsing NFB OLSON")

    def test_MR(self):
        f = os.path.join(wd, 'NFB_MR_212_000000_Pre.txt')
        correct = {'mrt1lmrt': '4568.600',
                    'mrt1lsdrt': '1689.976',
                    'mrt1ltc': '18',
                    'mrt1ltcp': '90.000',
                    'studyid': '212'}
        data = parse(f)
        self.assertEqual(data, correct, "Failed parsing NFB MR")

    def test_SENT(self):
        f = os.path.join(wd, 'NFB_SENT_157_000000.txt')
        correct = {'sctoc': '19',
					'sctso10mean': '1540.022',
					'sctso10sd': '474.219',
					'sctso11mean': '1676.846',
					'sctso11sd': '486.824',
					'sctso12mean': '1639.333',
					'sctso12sd': '457.377',
					'sctso1mean': '1560.500',
					'sctso1sd': '129.680',
					'sctso2mean': '1932.417',
					'sctso2sd': '470.967',
					'sctso3mean': '1684.000',
					'sctso3sd': '441.370',
					'sctso4mean': '2129.691',
					'sctso4sd': '1005.250',
					'sctso5mean': '1688.333',
					'sctso5sd': '231.177',
					'sctso6mean': '1630.658',
					'sctso6sd': '639.755',
					'sctso7mean': '1926.083',
					'sctso7sd': '745.401',
					'sctso8mean': '1717.833',
					'sctso8sd': '547.035',
					'sctso9mean': '1779.417',
					'sctso9sd': '389.411',
					'sctsotc': '8',
					'sctss01mrt': '1755.417',
					'sctss01sd': '107.614',
					'sctss02mrt': '1725.583',
					'sctss02sd': '270.288',
					'sctss03mrt': '1920.250',
					'sctss03sd': '266.853',
					'sctss04mrt': '1873.667',
					'sctss04sd': '272.755',
					'sctss05mrt': '1699.167',
					'sctss05sd': '242.364',
					'sctss06mrt': '1805.500',
					'sctss06sd': '382.794',
					'sctss07mrt': '1660.750',
					'sctss07sd': '451.682',
					'sctss08mrt': '1676.022',
					'sctss08sd': '780.089',
					'sctss09mrt': '1734.833',
					'sctss09sd': '323.817',
					'sctss10mrt': '1499.750',
					'sctss10sd': '283.809',
					'sctss11mrt': '1818.417',
					'sctss11sd': '590.310',
					'sctss12mrt': '1686.416',
					'sctss12sd': '751.857',
					'sctsstc': '11',
                    'studyid': '157'}
        data = parse(f)
        self.assertEqual(data, correct, "Failed parsing NFB SENT")
