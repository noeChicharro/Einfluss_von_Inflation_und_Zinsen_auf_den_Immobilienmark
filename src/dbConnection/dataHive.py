import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('data/dataHive.csv') ## nicht der originale Name
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS dataHive')

create_value_tabel = '''
CREATE TABLE dataHive (
    data_extraction_date DATE,
    vendor_master_public_id VARCHAR(255),
    vendor_master_name VARCHAR(255),
    vendor_master_address VARCHAR(255),
    classification VARCHAR(100),
    internal_ad_campaign_id VARCHAR(100),
    public_ad_campaign_id VARCHAR(100),
    activated DATE,
    inactivated DATE,
    update_time DATETIME,
    deleted BOOLEAN,
    on_market_in_days INT,
    price_calculated DECIMAL(15,2),
    purchase_price DECIMAL(15,2),
    net_rent DECIMAL(15,2),
    gross_rent DECIMAL(15,2),
    side_cost_calculated DECIMAL(15,2),
    price_per_sqr_meter DECIMAL(10,2),
    room_count DECIMAL(5,2),
    bathroom_count DECIMAL(5,2),
    area_living DECIMAL(10,2),
    area_property DECIMAL(10,2),
    gwr_area_property DECIMAL(10,2),
    gwr_energy_source_water VARCHAR(100),
    gwr_energy_source_heating VARCHAR(100),
    gwr_renovation_year YEAR,
    gwr_construction_year YEAR,
    gwr_floors INT,
    gwr_area_building DECIMAL(10,2),
    ax_rating_connectivity TINYINT,
    ax_rating_education TINYINT,
    ax_rating_immission TINYINT,
    ax_rating_leisure TINYINT,
    ax_rating_noise TINYINT,
    ax_overall_rating TINYINT,
    ax_rating_public_transportation TINYINT,
    ax_rating_service TINYINT,
    ax_rating_sun_exposure TINYINT,
    ax_rating_view TINYINT,
    nlp_is_temporary BOOLEAN,
    nlp_is_furnished BOOLEAN,
    building_volume DECIMAL(15,2),
    parking_count INT,
    garage_count INT,
    property_condition VARCHAR(100),
    built_year YEAR,
    floor_number INT,
    renovation_year YEAR,
    transaction_type VARCHAR(100),
    property_category VARCHAR(100),
    internal_property_category_id VARCHAR(100),
    property_type VARCHAR(100),
    public_property_type_id VARCHAR(100),
    site_id VARCHAR(100),
    site_name VARCHAR(255),
    entrance_address_id VARCHAR(100),
    street_id VARCHAR(100),
    street VARCHAR(255),
    street_number VARCHAR(20),
    zip VARCHAR(20),
    main_zip VARCHAR(20),
    locality_public_id VARCHAR(100),
    locality VARCHAR(255),
    ms_region_public_id VARCHAR(100),
    ms_region_label VARCHAR(255),
    ms_region_code VARCHAR(50),
    mr_region_public_id VARCHAR(100),
    mr_region_label VARCHAR(255),
    mr_region_code VARCHAR(50),
    labour_market_region_public_id VARCHAR(100),
    labour_market_region_label VARCHAR(255),
    labour_market_region_code VARCHAR(50),
    major_labour_market_region_public_id VARCHAR(100),
    major_labour_market_region_name VARCHAR(255),
    commune_public_id VARCHAR(100),
    commune_name VARCHAR(255),
    district VARCHAR(255),
    canton_public_id VARCHAR(100),
    canton VARCHAR(10),
    canton_name VARCHAR(100),
    latitude DECIMAL(10,7),
    longitude DECIMAL(10,7),
    geo_quality VARCHAR(50),
    min_price DECIMAL(15,2),
    max_price DECIMAL(15,2),
    initial_price DECIMAL(15,2),
    num_price_increase INT,
    num_price_decrease INT,
    num_price_changes INT,
    is_valid_for_statistics BOOLEAN
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('dataHive', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()

