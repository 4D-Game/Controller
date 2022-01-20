# Controller Setup

## Development

To write code and generate the documentation you need to install the packages listed in `requirements.txt` with `pip`

```bash
pip3 install -r requirements.txt
```

The sdk needed to use this program is stored in a submodule. To use it the following commands should be executed:

```bash
git submodule init
git submodule update
git submodule foreach --recursive 'git checkout master'
```

!!! INFO
    To update the sdk to the latest commit run

    ```bash
    git submodule foreach --recursive 'git pull'
    ```

### PYTHONPATH
To use the `4DGame` SDK you have do add the `lib` folder to your `PYTHONPATH` variable.
Additionally add the `src` folder to your `PYTHONPATH` for nicer imports and automatic documentation.

```bash
export PYTHONPATH="$(pwd)/src:$(pwd)/lib/sdk"
```
### Documentation
The Documentation is generated with the help of [mkdocstrings](https://mkdocstrings.github.io/#). To implement a module, class or function into your documentation you have to reference it as follows:

```md
::: library.module

::: library.module.class

::: library.module.function
```

## On Device

For the usage on Device the packages listed in `requirements.txt` should be installed:

```bash
pip install -r requirements.txt
```

Next setup the controller service with `scripts/systemd-setup`