\# Data Quality Pipeline



An automated data quality validation pipeline built with pandas and Great Expectations — designed as a bridge project between QA automation testing and data engineering.



\## What This Project Does



In QA, we validate that an \*application\* behaves correctly under edge cases. In data engineering, we validate that \*data\* is trustworthy before it's used for decisions — nulls where there shouldn't be, duplicates, values out of range, invalid categories. This pipeline automatically checks a real-world dataset for these issues and produces a pass/fail report, the same way an automated test suite checks an application.



\## Why I Built This



As an SDET/QA automation engineer, I wanted hands-on exposure to data engineering fundamentals. This project translates familiar QA concepts into a data validation context:



| QA Concept | Data Engineering Equivalent |

|---|---|

| Assertions / `@Test` checks | Great Expectations declarative rules |

| Boundary/equivalence testing | Range and type validation |

| Null/empty field validation | Completeness checks |

| Duplicate submission bugs | Uniqueness checks |

| Test report (e.g. Extent Report) | Great Expectations Data Docs (HTML report) |

| CI pipeline gating a build on test failure | GitHub Actions gating on data validation failure |



\## Dataset



A public insurance/health dataset (\~3,630 rows, sourced from Kaggle) with columns: `age`, `sex`, `bmi`, `smoker`, `region`, `children`, `charges`.



\## What I Found



\- \*\*1,893 rows (52%) had fractional `age` values\*\* (e.g. `36.976978`) — ages should always be whole numbers, so this represents a real underlying data quality issue.

\- All 9 declared expectations (nulls, valid ranges, valid categories) passed against the current dataset.

\- Verified the pipeline correctly \*catches\* violations by temporarily tightening the `bmi` range check — it correctly flagged 1,862 rows (51%) as out of range and reported the exact violating values.



\## Tech Stack



\- \*\*pandas\*\* — loads and explores the dataset as an in-memory DataFrame

\- \*\*Great Expectations\*\* — declares and runs data quality rules (Expectations) instead of manual `if` checks

\- \*\*GitHub Actions\*\* — runs the full validation pipeline automatically on every push, failing the build if any check fails (CI/CD-style data quality gate)



\## Project Structure

