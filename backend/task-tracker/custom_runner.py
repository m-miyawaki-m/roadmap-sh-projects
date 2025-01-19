import unittest
import csv
import os
import coverage

class CSVTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results.append({
            "test": str(test),
            "description": test.shortDescription(),
            "status": "SUCCESS",
            "error": ""
        })

    def addFailure(self, test, err):
        super().addFailure(test, err)
        error_message = self._exc_info_to_string(err, test)
        self.results.append({
            "test": str(test),
            "description": test.shortDescription(),
            "status": "FAILURE",
            "error": error_message
        })

    def addError(self, test, err):
        super().addError(test, err)
        error_message = self._exc_info_to_string(err, test)
        self.results.append({
            "test": str(test),
            "description": test.shortDescription(),
            "status": "ERROR",
            "error": error_message
        })


class CSVTestRunner(unittest.TextTestRunner):
    def __init__(self, output_csv="test_results.csv", coverage_report="coverage_report.txt", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_csv = output_csv
        self.coverage_report = coverage_report

    def _makeResult(self):
        return CSVTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        # カバレッジを開始
        cov = coverage.Coverage()
        cov.start()

        # テストを実行
        result = super().run(test)

        # カバレッジを停止し保存
        cov.stop()
        cov.save()

        # カバレッジレポートを生成
        with open(self.coverage_report, "w") as f:
            cov.report(file=f)
        print(f"Coverage report saved to {os.path.abspath(self.coverage_report)}")

        # テスト結果を CSV に保存
        self._write_csv(result.results)

        return result

    def _write_csv(self, results):
        fieldnames = ["test", "description", "status", "error"]
        with open(self.output_csv, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"Test summary saved to {os.path.abspath(self.output_csv)}")
