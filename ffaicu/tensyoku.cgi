#!/usr/bin/perl --

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͂����ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#  FF ADVENTURE(������)
#�@edit by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# syoku_regist�Ăяo��
require 'battle.pl';

# shopfooter�Ăяo��
require 'item.pl';

# ���̃t�@�C���p�ݒ�
$backgif = $shop_back;
$midi = $shop_midi;

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
if ($mente) {
	&error("�o�[�W�����A�b�v���ł��B�Q�A�R�O�b�قǂ��҂��������Bm(_ _)m");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="$script_tensyoku" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

if ($mode) { &$mode; }
&tensyoku;

exit;

#------------#
# �]�E�̐_�a #
#------------#
sub tensyoku {

	&chara_load;

	&chara_check;

	&syoku_load;

	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

$mitensyoku.="���ݓ]�E�ł���܂��}�X�^�[���Ă��Ȃ��E�Ƃ�<br><table><tr>";
$tensyokuok.= "���ݓ]�E�ł���E�Ƃ�<br><table><tr>";

	$i=0;$hit=0;$mhit=0;
	foreach (@syoku) {
		s/\n//i;
		s/\r//i;
		($a,$b,$c,$d,$e,$f,$g,$h) = split(/<>/);
		@pre = split(/<>/,$_,17);
		@syoku_require = split(/<>/,$pre[16]);
		if($chara[7] >= $a and $chara[8] >= $b and $chara[9] >= $c and $chara[10] >= $d and $chara[11] >= $e and $chara[12] >= $f and $chara[13] >= $g and $chara[20] >= $h and $chara[14] != $i) {
			$is=0;
			$shit=0;
			foreach (@syoku_require) {
				if ($_ > $syoku_master[$is]) {$shit = 1;}
				$is++;
			}
			if (!$shit) {
				$tensyokuok.="<td><font color=white size=3>\[$chara_syoku[$i]\]</font></td>";
				$selection.="<option value=\"$i\">$chara_syoku[$i]</option>\n";
				$hit+=1;
				if($hit % 5 == 0){$tensyokuok.="</tr><tr>";}
				if ($syoku_master[$i] < 60) {
					$mitensyoku.="<td><font color=white size=3>\[$chara_syoku[$i]\]</font></td>";
					$mhit+=1;
					if($mhit % 5 == 0){$mitensyoku.="</tr><tr>";}

				}
			}
		}
		$i++;
	}
	if(!$hit) { $tensyokuok.= "<td>����܂���</td>"; }
	if(!$mhit) { $mitensyoku.="<td>����܂���</td>"; }

	&header;

	print <<"EOM";
<h1>�]�E�̐_�a</h1><hr>
�����ł͑��̐E�Ƃɓ]�E�ł��܂��B<br>
�� �]�E����ƁA���݂̔\\�͒l�������_���ŉ�����܂��B�������A�]�E����E�Ƃ̐E�ƃ��x����20�ȏ�̏ꍇ�͉�����܂���B<br><br>
$tensyokuok</tr></table><br>
$mitensyoku</tr></table><br>
<form action="$script_tensyoku" method="post">
<select name=syoku>
<option value="no">�I�����Ă�������
$selection
</select>
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tensyoku_change">
<input type=submit class="btn" value="�]�E����">
</form>
<form action="$script" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#--------#
#  �]�E  #
#--------#
sub tensyoku_change {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'syoku'} eq 'no') {
		&error("�E�Ƃ�I�����Ă��������B$back_form");
	}

	$lock_file = "$lockfolder/syoku$in{'id'}.lock";
	&lock($lock_file,'SK');
	&syoku_load;

	$syoku_master[$chara[14]] = $chara[33];

	&syoku_regist;
	&unlock($lock_file,'SK');

	&get_host;

	open(IN,"$syoku_file");
	@syokudate = <IN>;
	close(IN);

	($a,$b,$c,$d,$e,$f,$g,$h) = split(/<>/,$syokudate[$in{'syoku'}]);
	$syokudate[$in{'syoku'}] =~ s/\n//gi;
	$syokudate[$in{'syoku'}] =~ s/\r//gi;

	if (!($chara[7] >= $a and $chara[8] >= $b and $chara[9] >= $c and $chara[10] >= $d and $chara[11] >= $e and $chara[12] >= $f and $chara[13] >= $g and $chara[20] >= $h) || !$syokudate[$in{'syoku'}]) {&error("�܂��]�E�ł��܂���");}

	$chara[14] = $in{'syoku'};
	if ($master_tac) { $chara[30] = 0; }	# �]�E��̐�p�N���A
	$chara[33] = $syoku_master[$chara[14]];

	if (!$chara[33]) { $chara[33] = 1; }

	if ($chara[33] < 20) {
		$chara[7] = int($chara[7]) - int($chara[7] / 10);
		$chara[8] = int($chara[8]) - int($chara[8] / 10);
		$chara[9] = int($chara[9]) - int($chara[9] / 10);
		$chara[10] = int($chara[10]) - int($chara[10] / 10);
		$chara[11] = int($chara[11]) - int($chara[11] / 10);
		$chara[12] = int($chara[12]) - int($chara[12] / 10);
		$chara[13] = int($chara[13]) - int($chara[13] / 10);
		$chara[20] = int($chara[20]) - int($chara[7] / 5);
		if($chara[7] < 9) { $chara[7] = 9; }
		if($chara[8] < 8) { $chara[8] = 8; }
		if($chara[9] < 8) { $chara[9] = 8; }
		if($chara[10] < 9) { $chara[10] = 9; }
		if($chara[11] < 9) { $chara[11] = 9; }
		if($chara[12] < 8) { $chara[12] = 8; }
		if($chara[13] < 8) { $chara[13] = 8; }
		if($chara[20]  < 0) { $chara[20] = 1; }
	}

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>$chara_syoku[$chara[14]]�ɓ]�E���܂���</h1><hr size=0>
<form action="$script" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&shopfooter;

	&footer;

	exit;
}
