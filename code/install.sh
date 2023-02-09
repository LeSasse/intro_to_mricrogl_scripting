#!/usr/bin/zsh

START_DIR=${PWD}

CODE_DIR=${START_DIR}/$(dirname ${0})
TMP_DIR=$(mktemp -d)

cd ${TMP_DIR}

SETUP_TEXT=$(cat) << EOF
# MRIcroGL
export PATH=\$PATH:/usr/local/MRIcroGL
alias mricrogl="MRIcroGL"
EOF

# check if the zshrc has been adjusted and if not add the lines
if grep -Fxq ${SETUP_TEXT} ~/.zshrc
then
  echo "No need to edit ~/.zshrc."
else
    # code if not found
    echo ${SETUP_TEXT} | tee -a ~/.zshrc 
fi

# download and install MRIcroGL
curl -fLO https://github.com/rordenlab/MRIcroGL/releases/latest/download/MRIcroGL_linux.zip
unzip MRIcroGL_linux.zip
cp ${CODE_DIR}/startup.py MRIcroGL/Resources/script/.
sudo cp -r -i MRIcroGL /usr/local/.

source ~/.zshrc

cd ${START_DIR}
rm -rf ${TMP_DIR}