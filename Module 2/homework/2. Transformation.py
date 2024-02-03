if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    clean_df = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    clean_df['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date


    columns_mapping = {
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    }

    clean_df = clean_df.rename(columns=columns_mapping)

    return clean_df


@test
def test_columns_names(output, *args) -> None:
    for col in output.columns:
        assert col == col.lower() and col.isidentifier(), f'Column name "{col}" is not in snake case'

@test
def test_passenger_count(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    
@test
def test_trip_distance(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero distance'