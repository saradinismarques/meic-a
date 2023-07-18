#!/bin/bash

mkdir -p compiled images

# ############ Convert friendly and compile to openfst ############
for i in friendly/*.txt; do
	echo "Converting friendly: $i"
   python3 compact2fst.py  $i  > sources/$(basename $i ".formatoAmigo.txt").txt
done


# ############ convert words to openfst ############
for w in tests/*.str; do
	echo "Converting words: $w"
	./word2fst.py `cat $w` > tests/$(basename $w ".str").txt
done


# ############ Compile source transducers ############
for i in sources/*.txt tests/*.txt; do
	echo "Compiling: $i"
    fstcompile --isymbols=syms.txt --osymbols=syms.txt $i | fstarcsort > compiled/$(basename $i ".txt").fst
done

# ############ CORE OF THE PROJECT  ############
fstcompose compiled/step1.fst compiled/step2.fst > compiled/step10.fst
fstcompose compiled/step10.fst compiled/step3.fst > compiled/step11.fst
fstcompose compiled/step11.fst compiled/step4.fst > compiled/step12.fst 
fstcompose compiled/step12.fst compiled/step5.fst > compiled/step13.fst
fstcompose compiled/step13.fst compiled/step6.fst > compiled/step14.fst
fstcompose compiled/step14.fst compiled/step7.fst > compiled/step15.fst
fstcompose compiled/step15.fst compiled/step8.fst > compiled/step16.fst
fstcompose compiled/step16.fst compiled/step9.fst > compiled/metaphoneLN.fst
fstinvert compiled/metaphoneLN.fst > compiled/invertMetaphoneLN.fst


############ generate PDFs  ############
echo "Starting to generate PDFs"
for i in compiled/*.fst; do
	echo "Creating image: images/$(basename $i '.fst').pdf"
   fstdraw --portrait --isymbols=syms.txt --osymbols=syms.txt $i | dot -Tpdf > images/$(basename $i '.fst').pdf
done



# ############ tests  ############
echo "Testing words"

for w in compiled/t-*.fst; do
    echo "Testing $w"
    
    fstcompose $w compiled/metaphoneLN.fst | fstshortestpath | fstproject --project_type=output |
    fstrmepsilon | fsttopsort | fstprint --acceptor --isymbols=./syms.txt
done
