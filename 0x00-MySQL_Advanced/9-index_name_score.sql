-- Create an index named 'idx_name_first_score'
CREATE INDEX idx_name_first_score
ON names (name(1), score);
