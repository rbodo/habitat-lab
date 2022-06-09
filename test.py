import sys

from habitat_baselines.run import run_exp
from habitat_baselines import phosphenes


def main():
    # os.chdir('/home/rbodo/PycharmProjects/habitat-lab/')

    # path_config = 'habitat_baselines/config/test/ppo_pointnav_test.yaml'
    path_config = 'habitat_baselines/config/pointnav/ppo_pointnav_example_bodo.yaml'

    run_exp(path_config, 'eval')


if __name__ == '__main__':

    main()

    sys.exit()
