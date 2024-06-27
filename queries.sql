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



DO $$
DECLARE
    query_text TEXT;
    result RECORD;
    col_name TEXT;
    tbl_name TEXT;
BEGIN
    FOR tbl_name IN
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    LOOP
        FOR col_name IN
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = tbl_name AND table_schema = 'public'
        LOOP
            IF col_name <> 'Sl. No' THEN
                query_text := 'SELECT "Sl. No", ''' || col_name || ''' AS null_column FROM "' || tbl_name || '" WHERE "' || col_name || '" IS NULL';
                
                -- Only the necessary output
                FOR result IN EXECUTE query_text
                LOOP
                    RAISE NOTICE 'Table: %, Sl. No: %, Null Column: %', tbl_name, result."Sl. No", result.null_column;
                END LOOP;
            END IF;
        END LOOP;
    END LOOP;
END $$;


