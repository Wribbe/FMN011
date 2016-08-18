import sys

def newton(x, f, df):
    """ Takes value x and strings f and df. Evaluate strings to functions and
    iterate over result until stop is reached through newtons method. """

    x = float(x)
    stop = 1.0*pow(10,-8)

    def single_iter(x):
        res_f = eval(f)
        res_df = eval(df)
        return x - res_f/res_df

    def current_eval(x):
        return eval(f)

    diff = 1
    new_x = x
    new_f = single_iter(x)
    while diff > stop:
        print("x: {}, f(x): {}".format(new_x, new_f))
        new_x = single_iter(new_x)
        new_f = current_eval(new_x)
        diff = abs(0-new_f)


def main(args):
    if 'newton' in args:
        newton(*args[1:])

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
