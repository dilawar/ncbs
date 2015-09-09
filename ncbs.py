"""ncbs.py: 

    Main script.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import logging

def do(args):
    if args.sync:
        import server
        logging.info("Syncing %s" % args.sync)
        server.sync_server(args)

def main():
    import argparse
    # Argument parser.
    description = '''description'''
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--sync', '-s'
        , required = False
        , type = str
        , help = 'Which server to sync.'
        )

    class Args: pass 
    args = Args()
    parser.parse_args(namespace=args)
    do(args)

if __name__ == '__main__':
    main()

