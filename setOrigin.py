#N4 Bias Field Correction
echo N4 bias for: $files
""" + antsLocation + """/N4BiasFieldCorrection \
-d 3 \
-i $files/acpc.nii \
-o [$files/corrected.nii.gz,$files/biasfield.nii.gz] \
-s 4 \
-b [200] \
-c [50x50x50x50,0.000001] 