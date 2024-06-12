# 0x00. MySQL Advanced

## Project Overview

This project covers advanced MySQL topics, including creating tables with constraints, optimizing queries with indexes, implementing stored procedures and functions, and creating triggers and views.

## Tasks

1. **We are all unique!**
   - Script: `0-uniq_users.sql`
   - Description: Create a table `users` with a unique constraint on the `email` field.

2. **In and not out**
   - Script: `1-country_users.sql`
   - Description: Extend the `users` table to include a `country` field with enum values.

3. **Best band ever!**
   - Script: `2-fans.sql`
   - Description: Rank countries by the number of fans for metal bands.

4. **Old school band**
   - Script: `3-glam_rock.sql`
   - Description: List bands with Glam rock as their main style, ranked by longevity.

5. **Buy buy buy**
   - Scripts: `4-init.sql`, `4-store.sql`, `4-main.sql`
   - Description: Create a trigger to decrease the quantity of an item after adding a new order.

6. **Email validation to sent**
   - Scripts: `5-init.sql`, `5-valid_email.sql`, `5-main.sql`
   - Description: Create a trigger to reset the `valid_email` attribute only when the email changes.

7. **Add bonus**
   - Scripts: `6-init.sql`, `6-bonus.sql`, `6-main.sql`
   - Description: Create a stored procedure `AddBonus` to add a new correction for a student.

8. **Average score**
   - Scripts: `7-init.sql`, `7-average_score.sql`, `7-main.sql`
   - Description: Create a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a student.

9. **Optimize simple search**
   - Script: `8-index_my_names.sql`
   - Description: Create an index on the `names` table for the first letter of the name.

## Setup

1. Start the MySQL service:
   ```bash
   service mysql start

