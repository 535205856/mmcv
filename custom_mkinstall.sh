echo y | pip3 uninstall mmcv
echo y | pip3 uninstall mmcv-full

#rm -fr ./build

export MMCV_WITH_OPS=1
export MAX_JOBS=8
source ./test/env_npu.sh

echo "---------build start---------"
python3 setup.py build_ext
echo "---------build end---------"
python3 setup.py develop
pip3.7 list | grep mmcv