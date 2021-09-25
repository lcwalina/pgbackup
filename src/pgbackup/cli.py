from argparse import Action, ArgumentParser

known_drivers = ['local', 's3']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error(f"Unknown driver. Available drivers are {known_drivers}")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help='URL of the PostgreSQL database to backup')
    parser.add_argument('--driver', '-d',
            help="how & where to store the backup",
            nargs=2,
            action=DriverAction,
            metavar=('driver', 'destination'),
            required=True
            )
    return parser

def main():
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 'local':
        outfile = open(args.destination, 'wb')
        print(f"Backing database up locally to {args.destination}")
        storage.local(dump.stdout, outfile)
