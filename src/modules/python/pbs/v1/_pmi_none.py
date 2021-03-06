
"""
/* 
# Copyright (C) 1994-2018 Altair Engineering, Inc.
# For more information, contact Altair at www.altair.com.
#
# This file is part of the PBS Professional ("PBS Pro") software.
#
# Open Source License Information:
#
# PBS Pro is free software. You can redistribute it and/or modify it under the
# terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# PBS Pro is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Commercial License Information:
#
# For a copy of the commercial license terms and conditions,
# go to: (http://www.pbspro.com/UserArea/agreement.html)
# or contact the Altair Legal Department.
#
# Altair’s dual-license business model allows companies, individuals, and
# organizations to create proprietary derivative works of PBS Pro and
# distribute them - whether embedded or bundled with other software -
# under a commercial license agreement.
#
# Use of Altair’s trademarks, including but not limited to "PBS™",
# "PBS Professional®", and "PBS Pro™" and Altair’s logos is subject to Altair's
# trademark licensing policies.
*      
*/
"""
__doc__ = """
This module is be used when no PMI is present.
"""

import pbs


class Pmi:
    def __init__(self, pyhome=None):
        pbs.logmsg(pbs.LOG_WARNING, "Stubbed PMI calls are being used")

    def _connect(self, endpoint, port):
        return

    def _disconnect(self):
        return

    def _get_usage(self, job):
        return None

    def _query(self, query_type):
        return None

    def _activate_profile(self, profile_name, job):
        return False

    def _deactivate_profile(self, job):
        return False

    def _pmi_power_off(self, hosts):
        return False

    def _pmi_power_on(self, hosts):
        return False

    def _pmi_ramp_down(self, hosts):
        return False

    def _pmi_ramp_up(self, hosts):
        return False
