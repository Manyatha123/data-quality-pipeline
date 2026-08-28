import great_expectations as gx
import sys

def run_data_quality_checks(csv_path):
    context = gx.get_context()

    data_source = context.data_sources.add_pandas("pipeline_datasource")
    data_asset = data_source.add_csv_asset("pipeline_data", csv_path)
    batch_definition = data_asset.add_batch_definition_whole_dataframe("full_data")
    batch = batch_definition.get_batch()
    validator = context.get_validator(batch=batch)

    # --- Your checks (same ones from your notebook) ---
    validator.expect_column_values_to_not_be_null("bmi")
    validator.expect_column_values_to_be_between("bmi", min_value=10, max_value=60)
    validator.expect_column_values_to_be_between("children", min_value=0, max_value=20)
    validator.expect_column_values_to_be_in_set("smoker", ["yes", "no"])
    validator.expect_column_values_to_be_in_set("sex", ["male", "female"])
    validator.expect_column_values_to_be_in_set(
        "region", ["northeast", "northwest", "southeast", "southwest"]
    )
    validator.expect_column_values_to_be_between("charges", min_value=0)
    validator.expect_column_values_to_not_be_null("age")
    validator.expect_column_values_to_not_be_null("charges")

    results = validator.validate()

    # --- Summary, like a test runner's final report ---
    total = len(results["results"])
    passed = sum(1 for r in results["results"] if r["success"])
    failed = total - passed

    print(f"\n{'='*40}")
    print(f"DATA QUALITY CHECK SUMMARY")
    print(f"{'='*40}")
    print(f"Total checks: {total}")
    print(f"Passed:       {passed}")
    print(f"Failed:       {failed}")
    print(f"{'='*40}\n")

    if failed > 0:
        print("FAILED CHECKS:")
        for r in results["results"]:
            if not r["success"]:
                print(f"  - {r['expectation_config']['type']} on column "
                      f"'{r['expectation_config']['kwargs'].get('column')}'")

    context.build_data_docs()
    context.open_data_docs()

    return failed == 0  # True if all checks passed

if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "data/Train_Data.csv"
    all_passed = run_data_quality_checks(csv_path)
    sys.exit(0 if all_passed else 1)