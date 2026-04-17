#!/usr/bin/env python3
import argparse
import csv
import json
import fileinput

def main(args):

    # p_timeline,databasename,tablename,row_object
    # 2025-08-29 15:48:09,panther_logs.public,aws_cloudtrail,"{""awsRegion"":""us-east-1"",""errorCode"":""ThrottlingException"",""eventSource"":""ecs.amazonaws.com"",""p_source_id"":""6695c5d9-625d-4853-9b23-15c5edb95449"",""p_source_label"":""Cloudtrail-organization"",""recipientAccountId"":""997658151025"",""errorMessage"":""Rate exceeded"",""p_log_type"":""AWS.CloudTrail"",""readOnly"":true,""userAgent"":""Amazon ECS Agent - v1.91.0 (*69e95d20) (linux) (+http://aws.amazon.com/ecs/)"",""userIdentity"":{""principalId"":""AROA6QSIPJBY5KI34N3K2:i-017551ee10d24fa41"",""sessionContext"":{""ec2RoleDelivery"":""2.0"",""sessionIssuer"":{""accountId"":""997658151025"",""arn"":""arn:aws:iam::997658151025:role/dev-vistar-ClusterInstanceRoleD85D9505-1VN4AWK105G2O"",""principalId"":""AROA6QSIPJBY5KI34N3K2"",""type"":""Role"",""userName"":""dev-vistar-ClusterInstanceRoleD85D9505-1VN4AWK105G2O""},""attributes"":{""creationDate"":""2025-08-29T11:31:51Z"",""mfaAuthenticated"":""false""}},""type"":""AssumedRole"",""accessKeyId"":""ASIA6QSIPJBYQL4UOGWT"",""accountId"":""997658151025"",""arn"":""arn:aws:sts::997658151025:assumed-role/dev-vistar-ClusterInstanceRoleD85D9505-1VN4AWK105G2O/i-017551ee10d24fa41""},""eventName"":""ListTagsForResource"",""eventTime"":""2025-08-29 15:48:09.000000000"",""p_parse_time"":""2025-08-29 15:48:21.372862790"",""requestID"":""488c6ea0-74d7-4629-a9c7-2b23f99f3ea6"",""managementEvent"":true,""p_any_ip_addresses"":[""52.200.0.87""],""p_source_file"":{""aws_s3_bucket"":""aws-controltower-logs-211125485097-us-east-1"",""aws_s3_key"":""o-yslhul5zqz/AWSLogs/o-yslhul5zqz/997658151025/CloudTrail/us-east-1/2025/08/29/997658151025_CloudTrail_us-east-1_20250829T1550Z_6J7awWij006bPPv2.json.gz""},""tlsDetails"":{""cipherSuite"":""TLS_AES_128_GCM_SHA256"",""clientProvidedHostHeader"":""ecs.us-east-1.amazonaws.com"",""tlsVersion"":""TLSv1.3""},""eventID"":""9115e33e-0f2d-45e1-b6a1-3314dbcf9464"",""p_any_aws_account_ids"":[""997658151025""],""p_any_aws_arns"":[""arn:aws:iam::997658151025:role/dev-vistar-ClusterInstanceRoleD85D9505-1VN4AWK105G2O"",""arn:aws:sts::997658151025:assumed-role/dev-vistar-ClusterInstanceRoleD85D9505-1VN4AWK105G2O/i-017551ee10d24fa41""],""p_any_trace_ids"":[""ASIA6QSIPJBYQL4UOGWT""],""p_event_time"":""2025-08-29 15:48:09.000000000"",""p_row_id"":""326d8cc42d6aa69fcbb096cf28f9de09"",""eventType"":""AwsApiCall"",""p_any_usernames"":[""dev-vistar-ClusterInstanceRoleD85D9505-1VN4AWK105G2O""],""eventCategory"":""Management"",""p_udm"":{""source"":{""ip"":""52.200.0.87"",""address"":""52.200.0.87""},""user"":{""arns"":[""arn:aws:iam::997658151025:role/dev-vistar-ClusterInstanceRoleD85D9505-1VN4AWK105G2O"",""arn:aws:sts::997658151025:assumed-role/dev-vistar-ClusterInstanceRoleD85D9505-1VN4AWK105G2O/i-017551ee10d24fa41""]}},""sourceIPAddress"":""52.200.0.87"",""eventVersion"":""1.11"",""p_any_actor_ids"":[""AROA6QSIPJBY5KI34N3K2"",""AROA6QSIPJBY5KI34N3K2:i-017551ee10d24fa41""],""p_schema_version"":0}"

    csv_reader = csv.reader(fileinput.input('-'))
    for line in csv_reader:
        if args.list_fields:
            row_data = json.loads(line[3])
            print("\n".join(row_data.keys()))
            break
        if args.fields:
            row_data = json.loads(line[3])
            filtered_data = {field: row_data.get(field, None) for field in args.fields}
            print(json.dumps(filtered_data, indent=2))
        else:
            print(json.loads(line[3]), indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consume and process exported csv logs from Panther")
    parser.add_argument('fields', nargs='*', help='Specific fields to extract from the row_object JSON')
    parser.add_argument('--list-fields', action='store_true', help='List all available fields in the row_object JSON')
    args = parser.parse_args()
    main(args)
