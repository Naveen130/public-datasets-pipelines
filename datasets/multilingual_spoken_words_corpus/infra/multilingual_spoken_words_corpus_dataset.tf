/**
 * Copyright 2021 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


resource "google_bigquery_dataset" "multilingual_spoken_words_corpus" {
  dataset_id  = "multilingual_spoken_words_corpus"
  project     = var.project_id
  description = "The Multilingual Spoken Words Corpus is a large and growing audio dataset of spoken words in 50 languages for academic research and commercial applications in keyword spotting and spoken term search. The dataset contains more than 340,000 keywords, totaling 23.4 million 1-second spoken examples (over 6,000 hours). The dataset has many use cases, ranging from voice-enabled consumer devices to call center automation. It was generated by applying forced alignment on crowd-sourced sentence-level audio to produce per-word timing estimates for extraction. All alignments are included in the dataset. Please see the paper(https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/fe131d7f5a6b38b23cc967316c13dae2-Paper-round2.pdf) for a detailed analysis of the contents of the data and methods for detecting potential outliers, along with baseline accuracy metrics on keyword spotting models trained from the dataset compared to models trained on a manually-recorded keyword dataset."
}

output "bigquery_dataset-multilingual_spoken_words_corpus-dataset_id" {
  value = google_bigquery_dataset.multilingual_spoken_words_corpus.dataset_id
}
