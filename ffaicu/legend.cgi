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
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �퓬���C�u�����̓ǂݍ���
require 'battle.pl';
# �����X�^�[��p���C�u����
require 'mbattle.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

if ($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");
	}
}

&boss;

exit;
#----------------------------#
#  ���W�F���h�v���C�X�ł̐퓬#
#----------------------------#
sub boss {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if (!$chara[25]) {
		&error("��x�L�����N�^�[�Ɠ����Ă�������");
	}

	if ($chara[32] < $in{'boss_file'}) {
		&error("�܂�����ł��܂���I");
	}

	$ntime = time();
	$b_time = $m_time;
	$ztime = $ntime - $chara[27];
	$ztime = $b_time - $ztime;

	if ($ztime > 0) { &legend_error; }

	&get_host;

	&item_load;

	&acs_add;

	$bmonster = "boss$in{'boss_file'}\_monster";

	open(IN,"$$bmonster");
	@MONSTER = <IN>;
	close(IN);

	$r_no = @MONSTER;

	$r_no = $chara[28];

	&mons_read;

	$khp_flg = $chara[15];
	$mhp = int(rand($mrand)) + $msp;
	$mhp_flg = $mhp;

	$i=1;
	$j=0;@battle_date=();
	foreach(1..$turn) {

		&shokika;

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;
		&mons_atowaza;

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	$kmori_w = $chara[28];

	&legend_sentoukeka;

	&acs_sub;

	&levelup;

	&hp_after;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$boss_h = int($boss /2);	
	if ($kmori_w == 1) {
		$backgif = $last_back;
		$midi = $last_boss_midi;
	} elsif ($kmori_w >= $boss_h) {
		$backgif = $boss_back;
		$midi = $boss_midi1;
	} else {
		$backgif = $boss2_back;
		$midi = $boss_midi2;
	}

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>���W�F���h�v���C�X</B></FONT><br>

<B><CENTER><FONT SIZE= "6">$mname</B>�����ꂽ�I</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&bossfooter;

	&footer;

	exit;
}

#--------------------------------#
#  ���W�F���h�v���C�X�p�t�b�^�[  #
#--------------------------------#
sub bossfooter {
	if ($win) { print "$comment$chara[4]�́A$mex�̌o���l����ɓ��ꂽ�B<b>$gold</b>G��ɓ��ꂽ�B<br>\n"; }
	else { print "$comment$chara[4]�́A$mex�̌o���l����ɓ��ꂽ�B������100���̂P�ɂȂ����E�E�E(��)<br>\n"; }

	if ($chara[28] != 0 && $win == 1) {
		print <<"EOM";
<form action="$script_legend" method="post">
<input type=hidden name="mode" value="boss">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="boss_file" value="$in{'boss_file'}">
<input type=submit class=btn value="����ɉ��ɐi��">
</form>
EOM
	}
	print <<"EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
}

#----------------#
#  �҂����ԕ\��  #
#----------------#
sub legend_error {

	foreach (keys %lock_flg) {
		if ($lock_flg{$_}) {
			if ($lockkey == 3) {
				foreach (@flock) {
					($flock_pre,$flock_file) = split(/,/);
					if ($flock_file eq $_) {
						last;
					}
				}
			}
			&unlock($_,$flock_pre);
		}
	}

	&header;

	&time_view;

       print <<"EOM";
<center><hr width=400>
<font color=red><B>�܂��퓬�ł��܂���I</B></font><br>
<FORM NAME= "form1">
����<INPUT TYPE= "text" NAME= "clock" SIZE= "3">�b�҂��ĉ�����
</FORM>
<form action= "$script_legend" method= "POST">
<input type= "hidden" name= "mode" value= "boss">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$in{'mydata'}">
<input type="hidden" name="boss_file" value="$in{'boss_file'}">
<input type= "submit" class= "btn" value= "���̐킢��">
</form>
<form action= "$script" method= "POST">
<input type= "hidden" name= "mode" value= "log_in">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$in{'mydata'}">
<input type= "submit" class= "btn" value= "�X�e�[�^�X��ʂ�">
</form>
<hr width=400>
</center>
EOM

	&footer;

	exit;

}
