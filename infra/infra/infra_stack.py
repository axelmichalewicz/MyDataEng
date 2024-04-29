from aws_cdk import Stack, aws_ecr, aws_events, aws_events_targets, aws_lambda
from constructs import Construct
from decouple import config


class BaseStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_ecr.Repository(
            self,
            id=f"repo-spotify-recommandation-{config('ENV')}",
            repository_name=f"repo-spotify-recommandation-{config('ENV')}",
            image_scan_on_push=True,
        )


class MainStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        spotify_lambda = aws_lambda.DockerImageFunction(
            self,
            id=f"spotify-recommandations-{config('ENV')}",
            function_name=f"spotify-recommandations-{config('ENV')}",
            code=aws_lambda.DockerImageCode.from_ecr(
                repository=aws_ecr.Repository.from_repository_name(
                    self,
                    id=f"repo-spotify-recommandation-{config('ENV')}",
                    repository_name=f"repo-spotify-recommandation-{config('ENV')}",
                )
            ),
            environment={
                "SPOTIFY_CLIENT_ID": f"{config('SPOTIFY_CLIENT_ID')}",
                "SPOTIFY_CLIENT_SECRET": f"{config('SPOTIFY_CLIENT_SECRET')}",
                "CHANNEL_KEY": f"{config('CHANNEL_KEY')}",
                "SLACK_BOT_TOKEN": f"{config('SLACK_BOT_TOKEN')}",
            },
        )

        rule = aws_events.Rule(
            self,
            id=f"rule-cron-spotify-{config('ENV')}",
            rule_name=f"rule-cron-spotify-{config('ENV')}",
            schedule=aws_events.Schedule.cron(minute="0", hour="7", month="*", week_day="*", year="*"),
        )
        rule.add_target(aws_events_targets.LambdaFunction(spotify_lambda))
