import sys
import csv
import netaddr
import ipaddress


class RangeToCidr(object):
    """
    Given a .CSV from Nirsoft.net, convert the IP ranges to newline-delimited
    CIDR blocks to STDOUT.
    """
    def __init__(self, csvFilePath):
        super(RangeToCidr, self).__init__()
        self.csvFilePath = csvFilePath
        self.ipRanges = None
        self.cidrs = None
        self.collapsedCidrs = None

    def load(self):
        self.ipRanges = []
        with open(self.csvFilePath, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                try:
                    self.ipRanges.append({'Start': row[0], 'End': row[1]})
                except IndexError:
                    pass
        return self

    def convert(self):
        self.cidrs = []
        self.collapsedCidrs = []
        for ipRange in self.ipRanges:
            for cidr in netaddr.iprange_to_cidrs(ipRange['Start'], ipRange['End']):
                self.cidrs.append(ipaddress.ip_network(cidr))
        for cidr in ipaddress.collapse_addresses(self.cidrs):
            self.collapsedCidrs.append(cidr)
        return self

    def print(self):
        for cidr in self.collapsedCidrs:
            print(cidr)

if len(sys.argv) != 2:
    exit('Usage: {0} PATH_TO_CSV'.format(sys.argv[0]))

RangeToCidr(sys.argv[1]).load().convert().print()
