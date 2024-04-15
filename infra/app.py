#!/usr/bin/env python3

import aws_cdk as cdk

from infra.infra_stack import BaseStack, MainStack

app = cdk.App()
BaseStack(app, "BaseStack")
MainStack(app, "MainStack")

app.synth()
