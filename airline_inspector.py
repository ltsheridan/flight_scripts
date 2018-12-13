import logging
import os
import pandas as pd
import sys as sys


def main(argv=None):
	"""
	Utilize Pandas library to read in both UNSD M49 country and area .csv file
	(tab delimited) as well as the UNESCO heritage site .csv file (tab delimited).
	Extract regions, sub-regions, intermediate regions, country and areas, and
	other column data.  Filter out duplicate values and NaN values and sort the
	series in alphabetical order. Write out each series to a .csv file for inspection.
	"""
	if argv is None:
		argv = sys.argv

	msg = [
		'Source file read and trimmed version written to file {0}',
		'Genres written to file {0}',
		'Platforms written to file {0}',
		'Publishers written to file {0}',
		'Ratings written to file {0}',
		'Developers written to file {0}'
	]

	# Setting logging format and default level
	logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

	# Read in source
	source_path = os.path.join('input', 'csv', 'aircrafts.csv')
	source_data_frame = read_csv(source_path, ',')
	source_data_frame_trimmed = trim_columns(source_data_frame)
	source_trimmed_csv = os.path.join('output', 'airlines', 'aircrafts_trimmed.csv')
	write_series_to_csv(source_data_frame_trimmed, source_trimmed_csv, ',', False)
	logging.info(msg[0].format(os.path.abspath(source_trimmed_csv)))

	source_path = os.path.join('input', 'csv', 'aircrafts.csv')
	source_data_frame = read_csv(source_path, ',')
	source_data_frame_trimmed = trim_columns(source_data_frame)
	source_trimmed_csv = os.path.join('output', 'airlines', 'aircrafts_trimmed.csv')
	write_series_to_csv(source_data_frame_trimmed, source_trimmed_csv, ',', False)
	logging.info(msg[0].format(os.path.abspath(source_trimmed_csv)))

	source_path = os.path.join('input', 'csv', 'aircrafts.csv')
	source_data_frame = read_csv(source_path, ',')
	source_data_frame_trimmed = trim_columns(source_data_frame)
	source_trimmed_csv = os.path.join('output', 'airlines', 'aircrafts_trimmed.csv')
	write_series_to_csv(source_data_frame_trimmed, source_trimmed_csv, ',', False)
	logging.info(msg[0].format(os.path.abspath(source_trimmed_csv)))

def extract_filtered_series(data_frame, column_name):
	"""
	Returns a filtered Panda Series one-dimensional ndarray from a targeted column.
	Duplicate values and NaN or blank values are dropped from the result set which is
	returned sorted (ascending).
	:param data_frame: Pandas DataFrame
	:param column_name: column name string
	:return: Panda Series one-dimensional ndarray
	"""

	return data_frame[column_name].str.strip().drop_duplicates().dropna().sort_values()
    # return data_frame[column_name].drop_duplicates().dropna().sort_values()


def read_csv(path, delimiter=','):
	"""
    Utilize Pandas to read in *.csv file.
    :param path: file path
    :param delimiter: field delimiter
    :return: Pandas DataFrame
    """
	# return pd.read_csv(path, sep=delimiter, engine='python')
	# return pd.read_csv(path, sep=delimiter, encoding='ISO-8859-1', engine='python')
	return pd.read_csv(path, sep=delimiter, encoding='utf-8', engine='python')


def trim_columns(data_frame):
	"""
	:param data_frame:
	:return: trimmed data frame
	"""
	trim = lambda x: x.strip() if type(x) is str else x
	return data_frame.applymap(trim)


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
