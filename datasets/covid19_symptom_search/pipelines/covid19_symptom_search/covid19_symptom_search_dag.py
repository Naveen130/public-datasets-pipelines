# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from airflow import DAG
from airflow.providers.cncf.kubernetes.operators import kubernetes_pod

default_args = {
    "owner": "Google",
    "depends_on_past": False,
    "start_date": "2022-11-30",
}


with DAG(
    dag_id="covid19_symptom_search.covid19_symptom_search",
    default_args=default_args,
    max_active_runs=1,
    schedule_interval="@daily",
    catchup=False,
    default_view="graph",
) as dag:

    # Storage transfer service
    sts = kubernetes_pod.KubernetesPodOperator(
        task_id="sts",
        startup_timeout_seconds=1000,
        name="load_data",
        namespace="composer",
        service_account_name="datasets",
        image_pull_policy="Always",
        image="{{ var.json.covid19_symptom_search.container_registry.run_transfer_service_kub }}",
        env_vars={
            "PROJECT_ID": "{{ var.value.gcp_project }}",
            "SOURCE_BUCKET": "covid-st-prod-datasets-bigquery",
            "SINK_BUCKET": "{{ var.value.composer_bucket }}",
            "GCS_PATH": "data/covid19_symptom_search/",
        },
        resources={
            "request_memory": "4G",
            "request_cpu": "1",
            "request_ephemeral_storage": "10G",
        },
    )

    # ETL within the kubernetes pod
    symptom_search_country_daily = kubernetes_pod.KubernetesPodOperator(
        task_id="symptom_search_country_daily",
        startup_timeout_seconds=1000,
        name="load_data",
        namespace="composer",
        service_account_name="datasets",
        image_pull_policy="Always",
        image="{{ var.json.covid19_symptom_search.container_registry.run_csv_transform_kub }}",
        env_vars={
            "DOWNLOAD_PATH": "",
            "SOURCE_GCS_KEY": '["country", "daily"]',
            "SOURCE_GCS_PATH": "data/covid19_symptom_search/ssd_i18n_expansion/",
            "DESTINATION_GCS_PATH": "data/covid19_symptom_search/symptom_search_country_daily/",
            "PROJECT_ID": "{{ var.value.gcp_project }}",
            "DATASET_ID": "covid19_symptom_search",
            "GCS_BUCKET": "{{ var.value.composer_bucket }}",
            "SCHEMA_FILEPATH": "schema.json",
            "TABLE_ID": "symptom_search_country_daily",
        },
        resources={
            "request_memory": "4G",
            "request_cpu": "1",
            "request_ephemeral_storage": "10G",
        },
    )

    # ETL within the kubernetes pod
    symptom_search_country_weekly = kubernetes_pod.KubernetesPodOperator(
        task_id="symptom_search_country_weekly",
        startup_timeout_seconds=1000,
        name="load_data",
        namespace="composer",
        service_account_name="datasets",
        image_pull_policy="Always",
        image="{{ var.json.covid19_symptom_search.container_registry.run_csv_transform_kub }}",
        env_vars={
            "DOWNLOAD_PATH": "",
            "SOURCE_GCS_KEY": '["country", "weekly"]',
            "SOURCE_GCS_PATH": "data/covid19_symptom_search/ssd_i18n_expansion/",
            "DESTINATION_GCS_PATH": "data/covid19_symptom_search/symptom_search_country_weekly/",
            "PROJECT_ID": "{{ var.value.gcp_project }}",
            "DATASET_ID": "covid19_symptom_search",
            "GCS_BUCKET": "{{ var.value.composer_bucket }}",
            "SCHEMA_FILEPATH": "schema.json",
            "TABLE_ID": "symptom_search_country_weekly",
        },
        resources={
            "request_memory": "4G",
            "request_cpu": "1",
            "request_ephemeral_storage": "10G",
        },
    )

    # ETL within the kubernetes pod
    symptom_search_sub_region_1_daily = kubernetes_pod.KubernetesPodOperator(
        task_id="symptom_search_sub_region_1_daily",
        startup_timeout_seconds=1000,
        name="load_data",
        namespace="composer",
        service_account_name="datasets",
        image_pull_policy="Always",
        image="{{ var.json.covid19_symptom_search.container_registry.run_csv_transform_kub }}",
        env_vars={
            "DOWNLOAD_PATH": "",
            "SOURCE_GCS_KEY": '["sub_region_1", "daily"]',
            "SOURCE_GCS_PATH": "data/covid19_symptom_search/ssd_i18n_expansion/",
            "DESTINATION_GCS_PATH": "data/covid19_symptom_search/symptom_search_sub_region_1_daily/",
            "PROJECT_ID": "{{ var.value.gcp_project }}",
            "DATASET_ID": "covid19_symptom_search",
            "GCS_BUCKET": "{{ var.value.composer_bucket }}",
            "SCHEMA_FILEPATH": "schema.json",
            "TABLE_ID": "symptom_search_sub_region_1_daily",
        },
        resources={
            "request_memory": "4G",
            "request_cpu": "1",
            "request_ephemeral_storage": "10G",
        },
    )

    # ETL within the kubernetes pod
    symptom_search_sub_region_1_weekly = kubernetes_pod.KubernetesPodOperator(
        task_id="symptom_search_sub_region_1_weekly",
        startup_timeout_seconds=1000,
        name="load_data",
        namespace="composer",
        service_account_name="datasets",
        image_pull_policy="Always",
        image="{{ var.json.covid19_symptom_search.container_registry.run_csv_transform_kub }}",
        env_vars={
            "DOWNLOAD_PATH": "",
            "SOURCE_GCS_KEY": '["sub_region_1", "weekly"]',
            "SOURCE_GCS_PATH": "data/covid19_symptom_search/ssd_i18n_expansion/",
            "DESTINATION_GCS_PATH": "data/covid19_symptom_search/symptom_search_sub_region_1_weekly/",
            "PROJECT_ID": "{{ var.value.gcp_project }}",
            "DATASET_ID": "covid19_symptom_search",
            "GCS_BUCKET": "{{ var.value.composer_bucket }}",
            "SCHEMA_FILEPATH": "schema.json",
            "TABLE_ID": "symptom_search_sub_region_1_weekly",
        },
        resources={
            "request_memory": "4G",
            "request_cpu": "1",
            "request_ephemeral_storage": "10G",
        },
    )

    # ETL within the kubernetes pod
    symptom_search_sub_region_2_weekly = kubernetes_pod.KubernetesPodOperator(
        task_id="symptom_search_sub_region_2_weekly",
        startup_timeout_seconds=1000,
        name="load_data",
        namespace="composer",
        service_account_name="datasets",
        image_pull_policy="Always",
        image="{{ var.json.covid19_symptom_search.container_registry.run_csv_transform_kub }}",
        env_vars={
            "DOWNLOAD_PATH": "",
            "SOURCE_GCS_KEY": '["sub_region_2", "weekly"]',
            "SOURCE_GCS_PATH": "data/covid19_symptom_search/ssd_i18n_expansion/",
            "DESTINATION_GCS_PATH": "data/covid19_symptom_search/symptom_search_sub_region_2_weekly/",
            "PROJECT_ID": "{{ var.value.gcp_project }}",
            "DATASET_ID": "covid19_symptom_search",
            "GCS_BUCKET": "{{ var.value.composer_bucket }}",
            "SCHEMA_FILEPATH": "schema.json",
            "TABLE_ID": "symptom_search_sub_region_2_weekly",
        },
        resources={
            "request_memory": "8G",
            "request_cpu": "2",
            "request_ephemeral_storage": "10G",
        },
    )

    sts >> [
        symptom_search_country_daily,
        symptom_search_country_weekly,
        symptom_search_sub_region_1_daily,
        symptom_search_sub_region_1_weekly,
        symptom_search_sub_region_2_weekly,
    ]
