import aws_cdk as core
import aws_cdk.assertions as assertions
from decouple import config

from infra.infra_stack import BaseStack, MainStack


def test_ecr_created():
    app = core.App()
    stack = BaseStack(app, "infra")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::ECR::Repository",
        {"RepositoryName": f"repo-spotify-recommandation-{config('ENV')}"},
    )


def test_lambdas_created():
    app = core.App()
    stack = MainStack(app, "infra")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Lambda::Function", 1)
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {"FunctionName": f"spotify-recommandations-{config('ENV')}"},
    )


def test_rules_created():
    app = core.App()
    stack = MainStack(app, "infra")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Events::Rule", 1)
    template.has_resource_properties("AWS::Events::Rule", {"Name": f"rule-cron-spotify-{config('ENV')}"})
