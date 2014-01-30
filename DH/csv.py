__author__ = 'Simon'

import csv


class Csv(object):

    __main_file = ""
    __csv_files = {}
    __cols_maps = {}

    def load_file(self, file_name, separator=";"):
        try:
            with open(file_name) as file:
                #strip .csv at the end
                file_alias = file_name[:str(file_name).rfind('.')].lower()

                self.__csv_files[file_alias] = (file_name, separator)

                if not self.main_file_exists:
                    self.set_main_file(file_alias)

                self.extract_cols(file_alias)

                return True
        except IOError:
            return False
        except TypeError:
            return False


    @property
    def main_file_exists(self):
        return self.__main_file != ""

    def set_main_file(self, file_alias):
        self.__main_file = file_alias

    def is_main_file(self, file_alias):
        return self.__main_file == file_alias

    def get_file_separator(self, file_alias):
        return self.__csv_files[file_alias][1]

    def get_file_name(self, file_alias):
        return self.__csv_files[file_alias][0]

    def extract_cols(self, file_alias):
        with open(self.get_file_name(file_alias)) as file:
            csv_reader = csv.reader(file, delimiter=self.get_file_separator(self.__main_file))
            cols_headers = ()
            for row in csv_reader:
                cols_headers = row
                break;

            cols_aliases = {}
            for index, col_header in enumerate(cols_headers):
                cols_aliases[col_header.strip()] = index

            self.__cols_maps[file_alias] = cols_aliases

    def get_cols_map(self, file_alias):
        return self.__cols_maps[file_alias]

    def get_longest_col_alias_len(self, file_alias):
        longest_alias_len = 0
        col_aliases = self.get_cols_map(file_alias)

        for col_alias in col_aliases:
            longest_alias_len = max(len(col_alias), longest_alias_len)

        return longest_alias_len

    def get_main_file_name(self):
        return self.__csv_files[self.__main_file][0]

    def preview(self, rows):
        output = ""
        with open(self.get_main_file_name()) as main_file:
            csv_reader = csv.reader(main_file, delimiter=self.get_file_separator(self.__main_file))
            for line, row in enumerate(csv_reader):
                output += ', '.join(row) + "\n"
                if line + 1 >= rows:
                    break

        return output

    def __str__(self):
        string = "Files:\n"
        for file_alias in sorted(self.__csv_files):

            longest_alias_len = self.get_longest_col_alias_len(file_alias)

            cols_aliases = self.get_cols_map(file_alias)
            csv_type = "##MAIN##" if(self.is_main_file(file_alias)) else ""

            string += '"{}"\n'.format(file_alias)
            string += csv_type + '\n'
            string += 'number of columns: ' + str(len(cols_aliases)) + "\n"
            string += 'column aliases:\n'
            for alias in sorted(cols_aliases):
                string += '{0:{1}}: {2}\n'.format(alias, longest_alias_len + 1, cols_aliases[alias])

            return string