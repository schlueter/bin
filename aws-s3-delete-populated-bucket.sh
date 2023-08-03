#!/usr/bin/env bash

BUCKET_NAME="$1"

epoch_of_s3_timestamp () {
    date -jf '%Y-%m-%d %H:%M:%S' "$1" +%s
}

epoch_30_days_ago () {
    echo $(($(date +%s)-$((30*24*60*60))))
}

get_all_files_in_bucket () {
    aws s3 --recursive ls "s3://$1"
}

while read -r LINE
do
    TIMESTAMP="$(awk '{print $1 " " $2}' <<<"$LINE")"
    echo "$TIMESTAMP" >/dev/null
    OBJECT_PATH="$(awk '{print $NF}' <<<"$LINE")"
    echo "$TIMESTAMP $OBJECT_PATH"
    aws s3 rm "s3://$BUCKET_NAME/$OBJECT_PATH"
done <<<"$(get_all_files_in_bucket "$BUCKET_NAME" | sort)"
aws s3api delete-bucket --bucket "$BUCKET_NAME"
