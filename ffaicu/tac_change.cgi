#!/usr/local/bin/perl --

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

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $sts_back;
$midi = $sts_midi;

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) { &error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B"); }
&decode;

	$back_form = << "EOM";
<br>
<form action="$scripts" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=hidden name=mode value="log_in">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

if($mode) { &$mode; }

&senjutu;

exit;

#----------------#
#  ��p�\��      #
#----------------#
sub senjutu {

	&chara_load;

	&chara_check;

	$hit=0;
	@log_senjutu = "0<>���ʂɐ키<>��p���g�p�����ɐ킢�܂�<>0<>\n";

	# ���݂̐E�Ƃ̐�p�̂�
	open(IN,"$tac_folder/tac$chara[14].ini");
	@gettac = <IN>;
	close(IN);
	foreach (@gettac){
		($ks_no,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
		if (!$ks_ms || ($ks_ms && $chara[33] >= 60)) {
			push(@log_senjutu,"$_");
			if($chara[30] eq "$ks_no"){
				$hit = 1;
				$now_tac = $ks_name;
				$now_tac_ex = $ks_plus;
			}
		}
	}

	#�}�X�^�[������p�̃C���N���[�h
	if ($master_tac) {
		&syoku_load;
		$i = 0;
		foreach (@syoku_master) {
			if ($_ >= 60 && $i != $chara[14]) {
				open(IN,"$tac_folder/tac$i.ini");
				@gettac = <IN>;
				close(IN);
				push(@log_senjutu,@gettac);
				foreach (@gettac){
					($ks_no,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
					if($chara[30] eq "$ks_no"){
						$hit = 1;
						$now_tac = $ks_name;
						$now_tac_ex = $ks_plus;
					}
				}
			}
			$i++;
		}
	}

	if(!$hit) {
		$now_tac = "���ʂɐ키";
		$now_tac_ex = "��p���g�p�����ɐ킢�܂�";
	}

	&header;

	print <<"EOM";
<h1>����c��</h1>
<hr size=0>
<BR>
<form action="$scripts" method="post">
<table>
<tr>
<th colspan=2>��p</th>
<tr><td class=b1>���݂̐�p</td><td class=b1>$now_tac</td><td class=b1>$now_tac_ex</td>
</tr>
EOM

	foreach(@log_senjutu){
		($s_no,$s_name,$s_ex,$s_mas) = split(/<>/);
		print "<tr>\n";
		print "<td class=b1><input type=radio name=senjutu_no value=\"$s_no\"></td><td class=b1>$s_name</td><td class=b1>$s_ex</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</tr>
</table>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=senjutu_henkou>
<input type=submit class=btn value="�ύX����">
</form>
<form action="$script" method="post">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#----------------#
#  ��p�ύX      #
#----------------#
sub senjutu_henkou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	@log_senjutu = "0<>���ʂɐ키<>0<>0<>\n";

	open(IN,"$tac_folder/tac$chara[14].ini");
	@gettac = <IN>;
	close(IN);
	foreach (@gettac){
		($ks_no,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
		# 2004�N7��7���C��
		if(!$ks_ms || ($ks_ms && $chara[33] >= 60)){
			push(@log_senjutu,"$_");
		}
	}

	#�}�X�^�[������p�̃C���N���[�h
	if ($master_tac) {
		&syoku_load;
		$i = 0;
		foreach (@syoku_master) {
			if ($_ >= 60 && $i != $chara[14]) {
				open(IN,"$tac_folder/tac$i.ini");
				@gettac = <IN>;
				close(IN);
				push(@log_senjutu,@gettac);
				foreach (@gettac){
					($ks_no,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
					if($chara[30] eq "$ks_no"){
						$hit = 1;
						$now_tac = $ks_name;
					}
				}
			}
			$i++;
		}
	}

	$hit=0;
	foreach(@log_senjutu){
		($s_no,$s_name) = split(/<>/);
		if($in{'senjutu_no'} eq "$s_no") { $hit=1;last; }
	}

	if(!$hit) { &error("����Ȑ�p�͂���܂���"); }

	&get_host;

	$chara[30] = $in{'senjutu_no'};

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>��p��$s_name�ɕύX���܂���</h1>
<hr size=0>
<form action="$script" method="post">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

