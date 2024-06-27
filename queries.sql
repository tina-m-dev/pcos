DO $$
DECLARE
    query_text TEXT;
BEGIN
    SELECT 'SELECT * FROM pcos WHERE ' || 
           string_agg('"' || column_name || '" IS NULL', ' OR ')
    INTO query_text
    FROM information_schema.columns
    WHERE table_name = 'pcos' AND table_schema = 'public'; -- Adjust schema if necessary
    
    RAISE NOTICE 'Executing query: %', query_text; -- Log the query being executed
    EXECUTE query_text;
END $$;
