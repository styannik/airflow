# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from typing import TYPE_CHECKING

from deprecated import deprecated

from airflow.auth.managers.fab.security_manager.override import FabAirflowSecurityManagerOverride

if TYPE_CHECKING:
    pass


@deprecated(
    reason="If you want to override the security manager, you should inherit from "
    "`airflow.auth.managers.fab.security_manager.override.FabAirflowSecurityManagerOverride` "
    "instead"
)
class AirflowSecurityManager(FabAirflowSecurityManagerOverride):
    """Placeholder, just here to avoid breaking the code of users who inherit from this.

    Do not use if writing new code.
    """

    ...
