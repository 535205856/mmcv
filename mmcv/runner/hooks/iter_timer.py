# BSD 3-Clause License
#
# Copyright (c) 2017 xxxx
# All rights reserved.
# Copyright 2021 Huawei Technologies Co., Ltd
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
import time

from .hook import HOOKS, Hook


@HOOKS.register_module()
class IterTimerHook(Hook):

    def before_epoch(self, runner):
        self.t = time.time()
        self.skip_step = 0  # added by jyl
        self.time_all = 0  # added by jyl

    def before_iter(self, runner):
        runner.log_buffer.update({'data_time': time.time() - self.t})

    def after_iter(self, runner):
        # runner.log_buffer.update({'time': time.time() - self.t})  # annoated by jyl
        cur_time = time.time()  # added by jyl
        runner.log_buffer.update({'time': cur_time - self.t})  # added by jyl
        if self.skip_step >= 5:  # added by jyl
            self.time_all += cur_time - self.t  # added by jyl
        self.skip_step += 1  # added by jyl
        self.t = time.time()
