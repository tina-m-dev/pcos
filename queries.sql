DO $$
DECLARE
    query_text TEXT;
    result RECORD;
BEGIN
    -- Generate the dynamic query
    SELECT 'SELECT * FROM pcos WHERE ' || 
           string_agg('"' || column_name || '" IS NULL', ' OR ')
    INTO query_text
    FROM information_schema.columns
    WHERE table_name = 'pcos' AND table_schema = 'public'; -- Adjust schema if necessary
    
    RAISE NOTICE 'Executing query: %', query_text; -- Log the query being executed

    -- Open a cursor to execute the dynamic query
    FOR result IN EXECUTE query_text
    LOOP
        -- Display each row
        RAISE NOTICE '%', row_to_json(result);
    END LOOP;
END $$;
