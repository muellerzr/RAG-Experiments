---
license: apache-2.0
language:
- en
---
## Preparing the dataset

### NOTICE:

All code is owned by Hugging Face and uses the Apache 2.0 Licence. While I clean and strip the dataset for processing, do note that this dataset is under the same scruteny as the original Apache 2.0 License.

## Clone Repo

Data souce used is the [accelerate](https://github.com/huggingface/accelerate) repository. I'm using the latest version, v0.25.0

```bash
git clone https://github.com/huggingface/accelerate
cd accelerate
git checkout v0.25.0
cd ..
mkdir docs src
mv accelerate/src/accelerate/* src
mv accelerate/docs/* docs
cd src
rm __init__.py commands/__init__.py test_utils/__init__.py utils/__init__.py
```

### Cleaning the dataset

Using `regex` in VSCODE, use the following replacement:

```regex
# Copyright(.*\n)+# limitations under the license.
```

```regex
<!--Copyright(.*\n)+-->
```

Then remove all import statements (as we only care about the content).