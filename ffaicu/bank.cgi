#!/usr/local/bin/perl

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͉��L��3�l�ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#�@FF ADVENTURE ��i v2.1
#�@programed by jun-k
#�@http://www5b.biglobe.ne.jp/~jun-kei/
#�@jun-kei@vanilla.freemail.ne.jp
#------------------------------------------------------#
#�@FF ADVENTURE v0.21
#�@programed by CUMRO
#�@http://cgi.members.interq.or.jp/sun/cumro/mm/
#�@cumro@sun.interq.or.jp
#------------------------------------------------------#
#  FF ADVENTURE(��) v1.021
#  remodeling by GUN
#  http://www2.to/meeting/
#  gun24@j-club.ne.jp
#------------------------------------------------------#
#  FF ADVENTURE(������)
#�@remodeling by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p���� #
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B     	#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B   	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B   	#
#---------------------------------------------------------------#
# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �A�C�e�����C�u�����̓ǂݍ���
require 'item.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $shop_back;
$midi = $shop_midi;

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="$script_bank" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("�A�N�Z�X�ł��܂���I�I");
	}
}

if($mode) { &$mode; }

&bank_shop;

exit;

#----------#
# ��s�\�� #
#----------#
sub bank_shop {

	&chara_load;

	&chara_check;

	if (!$chara[34]) { $chara[34] = 0; }

	if ($bank_max < $chara[34] + $chara[19]) {
		$bank_max_in = int(($bank_max - $chara[34]) / 1000);
	} else {
		$bank_max_in = int($chara[19] / 1000);
	}

	if ($gold_max < $chara[34] + $chara[19]) {
		$bank_max_out = int(($gold_max - $chara[19]) / 1000);
	} else {
		$bank_max_out = int($chara[34] / 1000);
	}

	&header;

	print <<"EOM";
<h1>��s</h1>
<hr size=0>
<font Size="3"> $chara[4]����̌��݂�<br>
�@�@�@�������F<b>$chara[19]</b>�M��  �^<br>
�@�@�@�@�@�@�@�a���\\�z�@�F<b><font color=$yellow>$bank_max_in\,000</font></b>�M��<br>
�@�@�@�a���@�F<b>$chara[34]</b>�M���^<br>
�@�@�@�@�@�@�@���o�\\�z  �F<b><font color=$yellow>$bank_max_out\,000</font></b>�M��
</font><br>
<font color=$yellow><b>�ō��a������z $bank_max�M��</b></font>�𒴂������͓�������c�̂Ɋ�t����܂��B<br>
<form action="$script_bank" method="post">
<input type="text" name="azuke" value="" size=10>000 �M��
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=bank_sell>
<input type=submit class=btn value="�M����a����">
</form>
<form action="$script_bank" method="post">
<input type="hidden" name="azuke" value="$bank_max_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=bank_sell>
<input type=submit class=btn value="�a����邾���a����">
</form>
<form action="$script_bank" method="post">
<input type="text" name=dasu value="" size=10>000 �M��
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=bank_buy>
<input type=submit class=btn value="�M�����o��">
</form>
<form action="$script_bank" method="post">
<input type="hidden" name=dasu value="$bank_max_out">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=bank_buy>
<input type=submit class=btn value="�o���邾���o��">
</form>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
# �������o�� #
#----------------#
sub bank_buy {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'dasu'} eq ""){
		&error("���z�����͂���Ă��܂���B$back_form");
	}

	if($in{'dasu'} =~ /[^0-9]/){
		&error('�G���[�I���l�s���̂��ߎ󂯕t���܂���');
	}

	if($in{'dasu'} <= 0) {
		&error("�}�C�i�X�͓��͏o���܂���B$back_form");
	} else {
		$dasuru = int($in{'dasu'}) * 1000;
	}

	if ($dasuru  > $chara[34]) {
		&error("�a���z�𒴂��Ă��܂��I�I$back_form");
	}

	if(!($in{'dasu'} > 0 && $in{'dasu'} <= $gold_max)) {
		&error("�s���Ȓl�ł��I");
	}

	&get_host;

	$chara[26] = $host;

	$chara[34] -= $dasuru;

	$chara[19] += $dasuru;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�����p���肪�Ƃ��������܂���</h1><br>
$dasuru�f�����o���܂����B
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
# ������a����   #
#----------------#
sub bank_sell {
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'azuke'} eq ""){
		&error("���z�����͂���Ă��܂���B$back_form");
	}

	if($in{'azuke'} =~ /[^0-9]/){
		&error('�G���[�I���l�s���̂��ߎ󂯕t���܂���');
	}

	if($in{'azuke'} <= 0) {
		&error("�}�C�i�X�͓��͏o���܂���B$back_form");
	} else {
		$azukeru = int($in{'azuke'}) * 1000;
	}

	if ($azukeru  > $chara[19]) {
		&error("�������𒴂��Ă��܂��I�I$back_form");
	}

	if(!($in{'azuke'} > 0 && $in{'azuke'} <= $gold_max)) {
		&error("�s���Ȓl�ł��I");
	}

	&get_host;

	$chara[26] = $host;

	$chara[34] += $azukeru;

	$chara[19] -= $azukeru;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�����p���肪�Ƃ��������܂���</h1><br>
$azukeru�f�a���܂����B
EOM

	&shopfooter;

	&footer;

	exit;
}

