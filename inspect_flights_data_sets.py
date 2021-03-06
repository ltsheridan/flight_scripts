import logging
import os
import pandas as pd
import sys as sys


def main(argv=None):
	"""
	Utilize Pandas library to read in both .csv files
	(tab delimited) as well as the UNESCO heritage site .csv file (tab delimited).
	Extract column data.  Filter out duplicate values and NaN values and sort the
	series in alphabetical order. Write out each series to a .csv file for inspection.
	"""
	if argv is None:
		argv = sys.argv

	msg = [
		'Source file read {0}',
		'Airports written to file {0}'
	]

	# Setting logging format and default level
	logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

	# Read in airports data set (tabbed separator)
	airports_csv = './input/csv/airports.csv'
	airports_data_frame = read_csv(airports_csv, '\t')
	logging.info(msg[0].format(os.path.abspath(airports_csv)))

	# Write airports to a .csv file.
	airports = extract_filtered_series(airports_data_frame, 'airport_name')
	airports_output_csv = './output/airports_output_csv'
	write_series_to_csv(airports, airports_output_csv, '\t', False)
	logging.info(msg[1].format(os.path.abspath(airports_output_csv)))

	# # Write sub-regions to a .csv file.
	# unsd_sub_region = extract_filtered_series(unsd_data_frame, 'sub_region_name')
	# unsd_sub_region_csv = './output/unsd_sub_region.csv'
	# write_series_to_csv(unsd_sub_region, unsd_sub_region_csv, '\t', False)
	# logging.info(msg[2].format(os.path.abspath(unsd_sub_region_csv)))
	#
	# # Write intermediate_regions to a .csv file.
	# unsd_intermed_region = extract_filtered_series(unsd_data_frame, 'intermediate_region_name')
	# unsd_intermed_region_csv = './output/unsd_intermed_region.csv'
	# write_series_to_csv(unsd_intermed_region, unsd_intermed_region_csv, '\t', False)
	# logging.info(msg[3].format(os.path.abspath(unsd_intermed_region_csv)))
	#
	# # Write countries or areas to a .csv file.
	# unsd_country_area = extract_filtered_series(unsd_data_frame, 'country_area_name')
	# unsd_country_area_csv = './output/unsd_country_area.csv'
	# write_series_to_csv(unsd_country_area, unsd_country_area_csv, '\t', False)
	# logging.info(msg[4].format(os.path.abspath(unsd_country_area_csv)))
	#
	# # Write development status to a .csv file.
	# unsd_dev_status = extract_filtered_series(unsd_data_frame, 'country_area_development_status')
	# unsd_dev_status_csv = './output/unsd_dev_status.csv'
	# write_series_to_csv(unsd_dev_status, unsd_dev_status_csv, '\t', False)
	# logging.info(msg[5].format(os.path.abspath(unsd_dev_status_csv)))
	#
	# # Read UNESCO heritage sites data (tabbed separator)
	# unesco_csv = './input/csv/unesco_heritage_sites.csv'
	# unesco_data_frame = read_csv(unesco_csv, '\t')
	# logging.info(msg[0].format(os.path.abspath(unesco_csv)))
	#
	# # Write UNESCO heritage site countries and areas to a .csv file
	# unesco_country_area = extract_filtered_series(unesco_data_frame, 'country_area')
	# unesco_country_area_csv = './output/unesco_heritage_site_country_area.csv'
	# write_series_to_csv(unesco_country_area, unesco_country_area_csv, '\t', False)
	# logging.info(msg[6].format(os.path.abspath(unesco_country_area_csv)))
	#
	# # Write UNESCO heritage site categories to a .csv file
	# unesco_site_category = extract_filtered_series(unesco_data_frame, 'category')
	# unesco_site_category_csv = './output/unesco_heritage_site_category.csv'
	# write_series_to_csv(unesco_site_category, unesco_site_category_csv, '\t', False)
	# logging.info(msg[7].format(os.path.abspath(unesco_site_category_csv)))
	#
	# # Write UNESCO heritage site regions to a .csv file
	# unesco_region = extract_filtered_series(unesco_data_frame, 'region')
	# unesco_region_csv = './output/unesco_heritage_site_region.csv'
	# write_series_to_csv(unesco_region, unesco_region_csv, '\t', False)
	# logging.info(msg[8].format(os.path.abspath(unesco_region_csv)))
	#
	# # Write UNESCO heritage site transboundary values to a .csv file
	# unesco_transboundary = extract_filtered_series(unesco_data_frame, 'transboundary')
	# unesco_transboundary_csv = './output/unesco_heritage_site_transboundary.csv'
	# write_series_to_csv(unesco_transboundary, unesco_transboundary_csv, '\t', False)
	# logging.info(msg[9].format(os.path.abspath(unesco_transboundary_csv)))

def trim_columns(data_frame):
	"""
	:param data_frame:
	:return: trimmed data frame
	"""
	trim = lambda x: x.strip() if type(x) is str else x
	return data_frame.applymap(trim)


def extract_filtered_series(data_frame, column_name):
	"""
	Returns a filtered Panda Series one-dimensional ndarray from a targeted column.
	Duplicate values and NaN or blank values are dropped from the result set which is
	returned sorted (ascending).
	:param data_frame: Pandas DataFrame
	:param column_name: column name string
	:return: Panda Series one-dimensional ndarray
	"""
	return data_frame[column_name].drop_duplicates().dropna().sort_values()


def read_csv(path, delimiter=','):
	"""
	Utilize Pandas to read in *.csv file.
	:param path: file path
	:param delimiter: field delimiter
	:return: Pandas DataFrame
	"""
	return pd.read_csv(path, sep=delimiter, engine='python')


def write_series_to_csv(series, path, delimiter=',', row_name=True):
	"""
	Write Pandas DataFrame to a *.csv file.
	:param series: Pandas one dimensional ndarray
	:param path: file path
	:param delimiter: field delimiter
	:param row_name: include row name boolean
	"""
	series.to_csv(path, sep=delimiter, index=row_name)


if __name__ == '__main__':
	sys.exit(main())
