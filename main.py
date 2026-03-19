import app.io.input as i
import app.io.output as o

def main():
    data_console = i.input_from_console()
    data_file = i.read_file("data.txt")
    data_file_pd = i.read_file_pd("data.csv")

    o.output_console(data_console)
    o.output_console(data_file)
    o.output_console(data_file_pd)

    o.write_file(data_console)
    o.write_file(data_file)
    o.write_file(data_file_pd)

if __name__ == '__main__':
    main()