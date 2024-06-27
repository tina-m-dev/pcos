DO $$
DECLARE
    query_text TEXT;
BEGIN
    SELECT 'SELECT * FROM your_table WHERE ' || 
           string_agg('"' || column_name || '" IS NULL', ' OR ')
    INTO query_text
    FROM information_schema.columns
    WHERE table_name = 'pcos_db' AND table_schema = 'public'; -- Adjust schema if necessary
    
    EXECUTE query_text;
END $$;
