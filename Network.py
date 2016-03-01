import pickle
class Network(object):

    def __init__(self, name):
        self.name = name
        self.nodes = dict()
        self.probability = dict()
        self.parents = dict()

    def add_node(self, name, node_type, levels, values):
        self.nodes[name] = (node_type, levels, values)

    def add_probability(self, child, parents, table):
        self.parents[child] = parents
        self.probability[child] = table

bn = Network('Alarm')
bn.add_node('HISTORY', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('CVP', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('PCWP', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('HYPOVOLEMIA', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('LVEDVOLUME', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('LVFAILURE', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('STROKEVOLUME', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('ERRLOWOUTPUT', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('HRBP', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('HREKG', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('ERRCAUTER', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('HRSAT', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('INSUFFANESTH', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('ANAPHYLAXIS', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('TPR', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('EXPCO2', 'discrete', 4, ('ZERO', 'LOW', 'NORMAL', 'HIGH'))
bn.add_node('KINKEDTUBE', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('MINVOL', 'discrete', 4, ('ZERO', 'LOW', 'NORMAL', 'HIGH'))
bn.add_node('FIO2', 'discrete', 2, ('LOW', 'NORMAL'))
bn.add_node('PVSAT', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('SAO2', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('PAP', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('PULMEMBOLUS', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('SHUNT', 'discrete', 2, ('NORMAL', 'HIGH'))
bn.add_node('INTUBATION', 'discrete', 3, ('NORMAL', 'ESOPHAGEAL', 'ONESIDED'))
bn.add_node('PRESS', 'discrete', 4, ('ZERO', 'LOW', 'NORMAL', 'HIGH'))
bn.add_node('DISCONNECT', 'discrete', 2, ('TRUE', 'FALSE'))
bn.add_node('MINVOLSET', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('VENTMACH', 'discrete', 4, ('ZERO', 'LOW', 'NORMAL', 'HIGH'))
bn.add_node('VENTTUBE', 'discrete', 4, ('ZERO', 'LOW', 'NORMAL', 'HIGH'))
bn.add_node('VENTLUNG', 'discrete', 4, ('ZERO', 'LOW', 'NORMAL', 'HIGH'))
bn.add_node('VENTALV', 'discrete', 4, ('ZERO', 'LOW', 'NORMAL', 'HIGH'))
bn.add_node('ARTCO2', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('CATECHOL', 'discrete', 2, ('NORMAL', 'HIGH'))
bn.add_node('HR', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('CO', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))
bn.add_node('BP', 'discrete', 3, ('LOW', 'NORMAL', 'HIGH'))

bn.add_probability('HISTORY', ['LVFAILURE'], [(('TRUE'), (0.9, 0.1)),
                                              (('FALSE'), (0.01, 0.99))])
bn.add_probability('CVP', ['LVEDVOLUME'], [(('LOW'), (0.95, 0.04, 0.01)),
                                           (('NORMAL'), (0.04, 0.95, 0.01)),
                                           ('HIGH'), (0.01, 0.29, 0.7)])
bn.add_probability('PCWP', ['LVFAILURE'], [(('LOW'), (0.95, 0.04, 0.01)),
                                           (('NORMAL'), (0.04, 0.95, 0.01)),
                                           ('HIGH'), (0.01, 0.04, 0.95)])
bn.add_probability('HYPOVOLEMIA', [None], [((None), (0.2, 0.8))])
bn.add_probability('LVEDVOLUME', ['HYPOVOLEMIA', 'LVFAILURE'], [(('TRUE', 'TRUE'), (0.95, 0.04, 0.01)),
                                                                (('FALSE', 'TRUE'), (0.98, 0.01, 0.01)),
                                                                (('TRUE', 'FALSE'), (0.01, 0.09, 0.9)),
                                                                (('FALSE', 'FALSE'), (0.05, 0.9, 0.05))])
bn.add_probability('LVFAILURE', [None], [((None), (0.05, 0.95))])
bn.add_probability('STROKEVOLUME', ['HYPOVOLEMIA', 'LVFAILURE'], [(('TRUE', 'TRUE'), (0.98, 0.01, 0.01)),
                                                                (('FALSE', 'TRUE'), (0.95, 0.04, 0.01)),
                                                                (('TRUE', 'FALSE'), (0.5, 0.49, 0.01)),
                                                                (('FALSE', 'FALSE'), (0.05, 0.9, 0.05))])
bn.add_probability('ERRLOWOUTPUT', [None], [((None), (0.05, 0.95))])
bn.add_probability('HRBP', ['ERRLOWOUTPUT', 'HR'], [(('TRUE', 'LOW'), (0.98, 0.01, 0.01)),
                                                    (('FALSE', 'LOW'), (0.4, 0.59, 0.01)),
                                                    (('TRUE', 'NORMAL'), (0.3, 0.4, 0.3)),
                                                    (('FALSE', 'NORMAL'), (0.98, 0.01, 0.01)),
                                                    (('TRUE', 'HIGH'), (0.01, 0.98, 0.01)),
                                                    (('FALSE', 'HIGH'), (0.01, 0.01, 0.98))])

bn.add_probability('HREKG', ['ERRCAUTER', 'HR'], [(('TRUE', 'LOW'), (0.33333334, 0.33333334, 0.33333334)),
                                                  (('FALSE', 'LOW'), (0.33333334, 0.33333334, 0.33333334)),
                                                  (('TRUE', 'NORMAL'), (0.33333334, 0.33333334, 0.33333334)),
                                                  (('FALSE', 'NORMAL'), (0.98, 0.01, 0.01)),
                                                  (('TRUE', 'HIGH'), (0.01, 0.98, 0.01)),
                                                  (('FALSE', 'HIGH'), (0.01, 0.01, 0.98))])
bn.add_probability('ERRCAUTER', [None], [((None), (0.1, 0.9))])
bn.add_probability('HRSAT', ['ERRCAUTER', 'HR'], [(('TRUE', 'LOW'), (0.33333334, 0.33333334, 0.33333334)),
                                                  (('FALSE', 'LOW'), (0.33333334, 0.33333334, 0.33333334)),
                                                  (('TRUE', 'NORMAL'), (0.33333334, 0.33333334, 0.33333334)),
                                                  (('FALSE', 'NORMAL'), (0.98, 0.01, 0.01)),
                                                  (('TRUE', 'HIGH'), (0.01, 0.98, 0.01)),
                                                  (('FALSE', 'HIGH'), (0.01, 0.01, 0.98))])
bn.add_probability('TPR', ['ANAPHYLAXIS'], [(('TRUE'), (0.98, 0.01, 0.01)),
                                            (('FALSE'), (0.3, 0.4, 0.3))])
bn.add_probability('INSUFFANESTH', [None], [((None), (0.1, 0.9))])
bn.add_probability('ANAPHYLAXIS', [None], [((None), (0.01, 0.99))])
bn.add_probability('EXPCO2', ['ARTCO2', 'VENTLUNG'], [(('LOW', 'ZERO'), (0.97, 0.01, 0.01, 0.01)),
                                                      (('NORMAL', 'ZERO'), (0.01, 0.97, 0.01, 0.01)),
                                                      (('HIGH', 'ZERO'), (0.01, 0.97, 0.01, 0.01)),
                                                      (('LOW', 'LOW'), (0.01, 0.97, 0.01, 0.01)),
                                                      (('NORMAL', 'LOW'), (0.97, 0.01, 0.01, 0.01)),
                                                      (('HIGH', 'LOW'), (0.01, 0.01, 0.97, 0.01)),
                                                      (('LOW', 'NORMAL'), (0.01, 0.01, 0.97, 0.01)),
                                                      (('NORMAL', 'NORMAL'), (0.01, 0.01, 0.97, 0.01)),
                                                      (('HIGH', 'NORMAL'), (0.97, 0.01, 0.01, 0.01)),
                                                      (('LOW', 'HIGH'), (0.01, 0.01, 0.01, 0.97)),
                                                      (('NORMAL', 'HIGH'), (0.01, 0.01, 0.01, 0.97)),
                                                      (('HIGH', 'HIGH'), (0.01, 0.01, 0.01, 0.97))])
bn.add_probability('KINKEDTUBE', [None], [((None), (0.04, 0.96))])
bn.add_probability('MINVOL', ['INTUBATION', 'VENTLUNG'], [(('NORMAL', 'ZERO'), (0.97, 0.01, 0.01, 0.01)),
                                                          (('ESOPHAGEAL', 'ZERO'), (0.01, 0.97, 0.01, 0.01)),
                                                          (('ONESIDED', 'ZERO'), (0.01, 0.01, 0.97, 0.01)),
                                                          (('NORMAL', 'LOW'), (0.01, 0.01, 0.01, 0.97)),
                                                          (('ESOPHAGEAL', 'LOW'), (0.97, 0.01, 0.01, 0.01)),
                                                          (('ONESIDED', 'LOW'), (0.6, 0.38, 0.01, 0.01)),
                                                          (('NORMAL', 'NORMAL'), (0.5, 0.48, 0.01, 0.01)),
                                                          (('ESOPHAGEAL', 'NORMAL'), (0.5, 0.48, 0.01, 0.01)),
                                                          (('ONESIDED', 'NORMAL'), (0.97, 0.01, 0.01, 0.01)),
                                                          (('NORMAL', 'HIGH'), (0.01, 0.97, 0.01, 0.01)),
                                                          (('ESOPHAGEAL', 'HIGH'), (0.01, 0.01, 0.97, 0.01)),
                                                          (('ONESIDED', 'HIGH'), (0.01, 0.01, 0.01, 0.97))])
bn.add_probability('FIO2', [None], [((None), (0.05, 0.95))])
bn.add_probability('PVSAT', ['FIO2', 'VENTALV'], [(('LOW', 'ZERO'), (1.0, 0.0, 0.0)),
                                                  (('NORMAL', 'ZERO'), (0.99, 0.01, 0.0)),
                                                  (('LOW', 'LOW'), (0.95, 0.04, 0.01)),
                                                  (('NORMAL', 'LOW'), (0.95, 0.04, 0.01)),
                                                  (('LOW', 'NORMAL'), (1.0, 0.0, 0.0)),
                                                  (('NORMAL', 'NORMAL'), (0.95, 0.04, 0.01)),
                                                  (('LOW', 'HIGH'), (0.01, 0.95, 0.04)),
                                                  (('NORMAL', 'HIGH'), (0.01, 0.01, 0.98))])
bn.add_probability('SAO2', ['PVSAT', 'SHUNT'], [(('LOW', 'NORMAL'), (0.98, 0.01, 0.01)),
                                                (('NORMAL', 'NORMAL'), (0.01, 0.98, 0.01)),
                                                (('HIGH', 'NORMAL'), (0.01, 0.01, 0.98)),
                                                (('LOW', 'HIGH'), (0.98, 0.01, 0.01)),
                                                (('NORMAL', 'HIGH'), (0.98, 0.01, 0.01)),
                                                (('HIGH', 'HIGH'), (0.69, 0.3, 0.01))])
bn.add_probability('PAP', ['PULMEMBOLUS'], [(('TRUE'), (0.01, 0.19, 0.8)),
                                            (('FALSE'), (0.05, 0.9, 0.05))])
bn.add_probability('PULMEMBOLUS', [None], [((None), (0.01, 0.99))])
bn.add_probability('SHUNT', ['INTUBATION', 'PULMEMBOLUS'], [(('NORMAL', 'TRUE'), (0.1, 0.9)),
                                                            (('ESOPHAGEAL', 'TRUE'), (0.1, 0.9)),
                                                            (('ONESIDED', 'TRUE'), (0.01, 0.99)),
                                                            (('NORMAL', 'FALSE'), (0.95, 0.05)),
                                                            (('ESOPHAGEAL', 'FALSE'), (0.95, 0.05)),
                                                            (('ONESIDED', 'FALSE'), (0.05, 0.95))])
bn.add_probability('INTUBATION', [None], [((None), (0.92, 0.03, 0.05))])
bn.add_probability('PRESS', ['INTUBATION', 'KINKEDTUBE', 'VENTTUBE'], [(('NORMAL', 'TRUE', 'ZERO'), (0.97, 0.01, 0.01,
                                                                                                     0.01)),
                                                                       (('ESOPHAGEAL', 'TRUE', 'ZERO'), (0.01, 0.3,
                                                                                                         0.49, 0.2)),
                                                                       (('ONESIDED', 'TRUE', 'ZERO'), (0.01, 0.01, 0.08,
                                                                                                       0.9)),
                                                                       (('NORMAL', 'FALSE', 'ZERO'), (0.01, 0.01, 0.01,
                                                                                                      0.97)),
                                                                       (('ESOPHAGEAL', 'FALSE', 'ZERO'), (0.97, 0.01,
                                                                                                          0.01, 0.01)),
                                                                       (('ONESIDED', 'FALSE', 'ZERO'), (0.1, 0.84, 0.05,
                                                                                                        0.01)),
                                                                       (('NORMAL', 'TRUE', 'LOW'), (0.05, 0.25, 0.25,
                                                                                                    0.45)),
                                                                       (('ESOPHAGEAL', 'TRUE', 'LOW'), (0.01, 0.15,
                                                                                                        0.25, 0.59)),
                                                                       (('ONESIDED', 'TRUE', 'LOW'), (0.97, 0.01, 0.01,
                                                                                                      0.01)),
                                                                       (('NORMAL', 'FALSE', 'LOW'), (0.01, 0.29, 0.3,
                                                                                                     0.4)),
                                                                       (('ESOPHAGEAL', 'FALSE', 'LOW'), (0.01, 0.01,
                                                                                                         0.08, 0.9)),
                                                                       (('ONESIDED', 'FALSE', 'LOW'), (0.01, 0.01, 0.01,
                                                                                                       0.97)),
                                                                       (('NORMAL', 'TRUE', 'NORMAL'), (0.97, 0.01, 0.01,
                                                                                                       0.01)),
                                                                       (('ESOPHAGEAL', 'TRUE', 'NORMAL'), (0.01, 0.97,
                                                                                                           0.01, 0.01)),
                                                                       (('ONESIDED', 'TRUE', 'NORMAL'), (0.01, 0.01,
                                                                                                         0.97, 0.01)),
                                                                       (('NORMAL', 'FALSE', 'NORMAL'), (0.01, 0.01,
                                                                                                        0.01, 0.97)),
                                                                       (('ESOPHAGEAL', 'FALSE', 'NORMAL'), (0.97, 0.01,
                                                                                                            0.01,
                                                                                                            0.01)),
                                                                       (('ONESIDED', 'FALSE', 'NORMAL'), (0.4, 0.58,
                                                                                                          0.01, 0.01)),
                                                                       (('NORMAL', 'TRUE', 'HIGH'), (0.2, 0.75, 0.04,
                                                                                                     0.01)),
                                                                       (('ESOPHAGEAL', 'TRUE', 'HIGH'), (0.2, 0.7, 0.09,
                                                                                                         0.01)),
                                                                       (('ONESIDED', 'TRUE', 'HIGH'), (0.97, 0.01, 0.01,
                                                                                                       0.01)),
                                                                       (('NORMAL', 'FALSE', 'HIGH'), (0.010000001,
                                                                                                      0.90000004,
                                                                                                      0.080000006,
                                                                                                      0.010000001)),
                                                                       (('ESOPHAGEAL', 'FALSE', 'HIGH'), (0.01, 0.01,
                                                                                                          0.38, 0.6)),
                                                                       (('ONESIDED', 'FALSE', 'HIGH'), (0.01, 0.01,
                                                                                                        0.01, 0.97))])
bn.add_probability('DISCONNECT', [None], [((None), (0.1, 0.9))])
bn.add_probability('MINVOLSET', [None], [((None), (0.05, 0.9, 0.05))])
bn.add_probability('VENTMACH', ['MINVOLSET'], [(('LOW'), (0.05, 0.93, 0.01, 0.01)),
                                           (('NORMAL'), (0.05, 0.01, 0.93, 0.01)),
                                           ('HIGH'), (0.05, 0.01, 0.01, 0.93)])
bn.add_probability('VENTTUBE', ['DISCONNECT', 'VENTMACH'], [(('TRUE', 'ZERO'), (0.97, 0.01, 0.01, 0.01)),
                                                            (('FALSE', 'ZERO'), (0.97, 0.01, 0.01, 0.01)),
                                                            (('TRUE', 'LOW'), (0.97, 0.01, 0.01, 0.01)),
                                                            (('FALSE', 'LOW'), (0.97, 0.01, 0.01, 0.01)),
                                                            (('TRUE', 'NORMAL'), (0.97, 0.01, 0.01, 0.01)),
                                                            (('FALSE', 'NORMAL'), (0.01, 0.97, 0.01, 0.01)),
                                                            (('TRUE', 'HIGH'), (0.01, 0.01, 0.97, 0.01)),
                                                            (('FALSE', 'HIGH'), (0.01, 0.01, 0.01, 0.97))])
bn.add_probability('VENTLUNG', ['INTUBATION', 'KINKEDTUBE', 'VENTTUBE'], [(('NORMAL', 'TRUE', 'ZERO'), (0.97, 0.01,
                                                                                                        0.01, 0.01)),
                                                                          (('ESOPHAGEAL', 'TRUE', 'ZERO'), (0.95000005,
                                                                                                            0.030000001,
                                                                                                            0.010000001,
                                                                                                            0.010000001)
                                                                           ),
                                                                          (('ONESIDED', 'TRUE', 'ZERO'), (0.4, 0.58,
                                                                                                          0.01, 0.01)),
                                                                          (('NORMAL', 'FALSE', 'ZERO'), (0.3, 0.68,
                                                                                                         0.01, 0.01)),
                                                                          (('ESOPHAGEAL', 'FALSE', 'ZERO'), (0.97, 0.01,
                                                                                                             0.01, 0.01)
                                                                           ),
                                                                          (('ONESIDED', 'FALSE', 'ZERO'), (0.97, 0.01,
                                                                                                           0.01, 0.01)),
                                                                          (('NORMAL', 'TRUE', 'LOW'), (0.97, 0.01, 0.01,
                                                                                                       0.01)),
                                                                          (('ESOPHAGEAL', 'TRUE', 'LOW'), (0.97, 0.01,
                                                                                                           0.01, 0.01)),
                                                                          (('ONESIDED', 'TRUE', 'LOW'), (0.97, 0.01,
                                                                                                         0.01, 0.01)),
                                                                          (('NORMAL', 'FALSE', 'LOW'), (0.95000005,
                                                                                                        0.030000001,
                                                                                                        0.010000001,
                                                                                                        0.010000001)),
                                                                          (('ESOPHAGEAL', 'FALSE', 'LOW'), (0.5, 0.48,
                                                                                                            0.01, 0.01)
                                                                           ),
                                                                          (('ONESIDED', 'FALSE', 'LOW'), (0.3, 0.68,
                                                                                                          0.01, 0.01)),
                                                                          (('NORMAL', 'TRUE', 'NORMAL'), (0.97, 0.01,
                                                                                                          0.01, 0.01)),
                                                                          (('ESOPHAGEAL', 'TRUE', 'NORMAL'), (0.01,
                                                                                                              0.97,
                                                                                                              0.01,
                                                                                                              0.01)),
                                                                          (('ONESIDED', 'TRUE', 'NORMAL'), (0.01, 0.01,
                                                                                                            0.97, 0.01)
                                                                           ),
                                                                          (('NORMAL', 'FALSE', 'NORMAL'), (0.01, 0.01,
                                                                                                           0.01, 0.97)),
                                                                          (('ESOPHAGEAL', 'FALSE', 'NORMAL'), (0.97,
                                                                                                               0.01,
                                                                                                               0.01,
                                                                                                               0.01)),
                                                                          (('ONESIDED', 'FALSE', 'NORMAL'), (0.97, 0.01,
                                                                                                             0.01, 0.01)
                                                                           ),
                                                                          (('NORMAL', 'TRUE', 'HIGH'), (0.97, 0.01,
                                                                                                        0.01, 0.01)),
                                                                          (('ESOPHAGEAL', 'TRUE', 'HIGH'), (0.97, 0.01,
                                                                                                            0.01, 0.01)
                                                                           ),
                                                                          (('ONESIDED', 'TRUE', 'HIGH'), (0.97, 0.01,
                                                                                                          0.01, 0.01)),
                                                                          (('NORMAL', 'FALSE', 'HIGH'), (0.01, 0.97,
                                                                                                         0.01, 0.01)),
                                                                          (('ESOPHAGEAL', 'FALSE', 'HIGH'), (0.01, 0.01,
                                                                                                             0.97, 0.01)
                                                                           ),
                                                                          (('ONESIDED', 'FALSE', 'HIGH'), (0.01, 0.01,
                                                                                                           0.01, 0.97))
                                                                          ])
bn.add_probability('VENTALV', ['INTUBATION', 'VENTLUNG'], [(('NORMAL', 'ZERO'), (0.97, 0.01, 0.01, 0.01)),
                                                           (('ESOPHAGEAL', 'ZERO'), (0.01, 0.97, 0.01, 0.01)),
                                                           (('ONESIDED', 'ZERO'), (0.01, 0.01, 0.97, 0.01)),
                                                           (('NORMAL', 'LOW'), (0.01, 0.01, 0.01, 0.97)),
                                                           (('ESOPHAGEAL', 'LOW'), (0.97, 0.01, 0.01, 0.01)),
                                                           (('ONESIDED', 'LOW'), (0.01, 0.97, 0.01, 0.01)),
                                                           (('NORMAL', 'NORMAL'), (0.01, 0.01, 0.97, 0.01)),
                                                           (('ESOPHAGEAL', 'NORMAL'), (0.01, 0.01, 0.01, 0.97)),
                                                           (('ONESIDED', 'NORMAL'), (0.97, 0.01, 0.01, 0.01)),
                                                           (('NORMAL', 'HIGH'), (0.030000001, 0.95000005, 0.010000001,
                                                                                 0.010000001)),
                                                           (('ESOPHAGEAL', 'HIGH'), (0.01, 0.94, 0.04, 0.01)),
                                                           (('ONESIDED', 'HIGH'), (0.01, 0.88, 0.1, 0.01))])
bn.add_probability('ARTCO2', ['VENTALV'], [(('ZERO'), (0.01, 0.01, 0.98)),
                                           (('LOW'), (0.01, 0.01, 0.98)),
                                           (('NORMAL'), (0.04, 0.92, 0.04)),
                                           ('HIGH'), (0.9, 0.09, 0.01)])
bn.add_probability('CATECHOL', ['ARTCO2', 'INSUFFANESTH', 'SAO2', 'TPR'],
                   [(('LOW', 'TRUE', 'LOW', 'LOW'), (0.01, 0.99)),
                    (('NORMAL', 'TRUE', 'LOW', 'LOW'), (0.01, 0.99)),
                    (('HIGH', 'TRUE', 'LOW', 'LOW'), (0.01, 0.99)),
                    (('LOW', 'FALSE', 'LOW', 'LOW'), (0.01, 0.99)),
                    (('NORMAL', 'FALSE', 'LOW', 'LOW'), (0.01, 0.99)),
                    (('HIGH', 'FALSE', 'LOW', 'LOW'), (0.01, 0.99)),
                    (('LOW', 'TRUE', 'NORMAL', 'LOW'), (0.01, 0.99)),
                    (('NORMAL', 'TRUE', 'NORMAL', 'LOW'), (0.01, 0.99)),
                    (('HIGH', 'TRUE', 'NORMAL', 'LOW'), (0.01, 0.99)),
                    (('LOW', 'FALSE', 'NORMAL', 'LOW'), (0.01, 0.99)),
                    (('NORMAL', 'FALSE', 'NORMAL', 'LOW'), (0.01, 0.99)),
                    (('HIGH', 'FALSE', 'NORMAL', 'LOW'), (0.01, 0.99)),
                    (('LOW', 'TRUE', 'HIGH', 'LOW'), (0.01, 0.99)),
                    (('NORMAL', 'TRUE', 'HIGH', 'LOW'), (0.01, 0.99)),
                    (('HIGH', 'TRUE', 'HIGH', 'LOW'), (0.01, 0.99)),
                    (('LOW', 'FALSE', 'HIGH', 'LOW'), (0.05, 0.95)),
                    (('NORMAL', 'FALSE', 'HIGH', 'LOW'), (0.05, 0.95)),
                    (('HIGH', 'FALSE', 'HIGH', 'LOW'), (0.01, 0.99)),
                    (('LOW', 'TRUE', 'LOW', 'NORMAL'), (0.01, 0.99)),
                    (('NORMAL', 'TRUE', 'LOW', 'NORMAL'), (0.01, 0.99)),
                    (('HIGH', 'TRUE', 'LOW', 'NORMAL'), (0.01, 0.99)),
                    (('LOW', 'FALSE', 'LOW', 'NORMAL'), (0.05, 0.95)),
                    (('NORMAL', 'FALSE', 'LOW', 'NORMAL'), (0.05, 0.95)),
                    (('HIGH', 'FALSE', 'LOW', 'NORMAL'), (0.01, 0.99)),
                    (('LOW', 'TRUE', 'NORMAL', 'NORMAL'), (0.05, 0.95)),
                    (('NORMAL', 'TRUE', 'NORMAL', 'NORMAL'), (0.05, 0.95)),
                    (('HIGH', 'TRUE', 'NORMAL', 'NORMAL'), (0.01, 0.99)),
                    (('LOW', 'FALSE', 'NORMAL', 'NORMAL'), (0.05, 0.95)),
                    (('NORMAL', 'FALSE', 'NORMAL', 'NORMAL'), (0.05, 0.95)),
                    (('HIGH', 'FALSE', 'NORMAL', 'NORMAL'), (0.01, 0.99)),
                    (('LOW', 'TRUE', 'HIGH', 'NORMAL'), (0.05, 0.95)),
                    (('NORMAL', 'TRUE', 'HIGH', 'NORMAL'), (0.05, 0.95)),
                    (('HIGH', 'TRUE', 'HIGH', 'NORMAL'), (0.01, 0.99)),
                    (('LOW', 'FALSE', 'HIGH', 'NORMAL'), (0.05, 0.95)),
                    (('NORMAL', 'FALSE', 'HIGH', 'NORMAL'), (0.05, 0.95)),
                    (('HIGH', 'FALSE', 'HIGH', 'NORMAL'), (0.01, 0.99)),
                    (('LOW', 'TRUE', 'LOW', 'HIGH'), (0.7, 0.3)),
                    (('NORMAL', 'TRUE', 'LOW', 'HIGH'), (0.7, 0.3)),
                    (('HIGH', 'TRUE', 'LOW', 'HIGH'), (0.1, 0.9)),
                    (('LOW', 'FALSE', 'LOW', 'HIGH'), (0.7, 0.3)),
                    (('NORMAL', 'FALSE', 'LOW', 'HIGH'), (0.7, 0.3)),
                    (('HIGH', 'FALSE', 'LOW', 'HIGH'), (0.1, 0.9)),
                    (('LOW', 'TRUE', 'NORMAL', 'HIGH'), (0.7, 0.3)),
                    (('NORMAL', 'TRUE', 'NORMAL', 'HIGH'), (0.7, 0.3)),
                    (('HIGH', 'TRUE', 'NORMAL', 'HIGH'), (0.1, 0.9)),
                    (('LOW', 'FALSE', 'NORMAL', 'HIGH'), (0.95, 0.05)),
                    (('NORMAL', 'FALSE', 'NORMAL', 'HIGH'), (0.99, 0.01)),
                    (('HIGH', 'FALSE', 'NORMAL', 'HIGH'), (0.3, 0.7)),
                    (('LOW', 'TRUE', 'HIGH', 'HIGH'), (0.95, 0.05)),
                    (('NORMAL', 'TRUE', 'HIGH', 'HIGH'), (0.99, 0.01)),
                    (('HIGH', 'TRUE', 'HIGH', 'HIGH'), (0.3, 0.7)),
                    (('LOW', 'FALSE', 'HIGH', 'HIGH'), (0.95, 0.05)),
                    (('NORMAL', 'FALSE', 'HIGH', 'HIGH'), (0.99, 0.01)),
                    (('HIGH', 'FALSE', 'HIGH', 'HIGH'), (0.3, 0.7))])
bn.add_probability('HR', ['CATECHOL'], [(('NORMAL'), (0.05, 0.9, 0.05)),
                                        (('HIGH'), (0.01, 0.09, 0.9))])
bn.add_probability('CO', ['HR', 'STROKEVOLUME'], [(('LOW', 'LOW'), (0.98, 0.01, 0.01)),
                                                  (('NORMAL', 'LOW'), (0.95, 0.04, 0.01)),
                                                  (('HIGH', 'LOW'), (0.8, 0.19, 0.01)),
                                                  (('LOW', 'NORMAL'), (0.95, 0.04, 0.01)),
                                                  (('NORMAL', 'NORMAL'), (0.04, 0.95, 0.01)),
                                                  (('HIGH', 'NORMAL'), (0.01, 0.04, 0.95)),
                                                  (('LOW', 'HIGH'), (0.3, 0.69, 0.01)),
                                                  (('NORMAL', 'HIGH'), (0.01, 0.3, 0.69)),
                                                  (('HIGH', 'HIGH'), (0.01, 0.01, 0.98))])
bn.add_probability('BP', ['CO', 'TPR'], [(('LOW', 'LOW'), (0.98, 0.01, 0.01)),
                                         (('NORMAL', 'LOW'), (0.98, 0.01, 0.01)),
                                         (('HIGH', 'LOW'), (0.9, 0.09, 0.01)),
                                         (('LOW', 'NORMAL'), (0.98, 0.01, 0.01)),
                                         (('NORMAL', 'NORMAL'), (0.1, 0.85, 0.05)),
                                         (('HIGH', 'NORMAL'), (0.05, 0.2, 0.75)),
                                         (('LOW', 'HIGH'), (0.3, 0.6, 0.1)),
                                         (('NORMAL', 'HIGH'), (0.05, 0.4, 0.55)),
                                         (('HIGH', 'HIGH'), (0.01, 0.09, 0.9))])