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

# ���̃t�@�C���p�ݒ�
$temp_back = "$mode\_back";
$temp_midi = "$mode\_midi";
$backgif = $$temp_back;
$midi = $$temp_midi;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");
	}
}

&$mode;

exit;

#----------------------#
#  �����X�^�[�Ƃ̐퓬  #
#----------------------#
sub monster {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if (!$chara[25]) {
		&error("��x�L�����N�^�[�Ɠ����Ă�������");
	}

	&time_check;

	&item_load;

	&acs_add;

	$monster_file = "$in{'mons_file'}\_monster";

	open(IN,"$$monster_file");
	@MONSTER = <IN>;
	close(IN);

	$r_no = @MONSTER;

	$r_no = int(rand($r_no));

	&mons_read;

	$khp_flg = $chara[15];
	$mhp = int(rand($mrand)) + $msp;
	$mhp_flg = $mhp;
	$m_sp = int(rand(11));

	$i=1;
	$j=0;
	@battle_date=();
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

	&sentoukeka;

	&acs_sub;

	&levelup;

	&hp_after;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print "<h1>$chara[4]�́A$mname�ɐ킢�𒧂񂾁I�I</h1><hr size=0>\n";

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&mons_footer;

	&footer;

	exit;
}

#----------------------#
#  ���e�̏�̐퓬      #
#----------------------#
sub genei {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if (!$chara[25]) {
		&error("��x�L�����N�^�[�Ɠ����Ă�������");
	}

	&time_check;

	if ($chara[27]%5 != 0) {
		&error("���������Ă��܂��čs���܂���ł���");
	}

	&item_load;

	&acs_add;


	if ($chara[18] < $genei_low) {
		$monster_file=$monster0_monster;
	}
	elsif ($chara[18] < $genei_high) {
		$monster_file=$monster1_monster;
	}
	elsif ($chara[18] < $genei_max) {
		$monster_file=$monster2_monster;
	}
	else {
		$monster_file=$monster3_monster;
	}

	open(IN,"$monster_file");
	@MONSTER = <IN>;
	close(IN);

	$r_no = @MONSTER;

	$r_no = int(rand($r_no));

	&mons_read;

	$khp_flg = $chara[15];
	$mhp = int(rand($mrand)) + $msp * 2;
	$mhp_flg = $mhp;

	$i=1;
	$j=0;@battle_date=();
	foreach(1..$turn) {

		&shokika;

		$dmg2 += $item[4];

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;

	if ($win == 1) {
		if (int(rand(3)) == 0) {
			$otakara = int(rand(1000)+1) * int($mgold);
			$chara[19] += $otakara;
			$comment .= "<b><font size=5 color=red>����($otakara�f)�𔭌������I�I�I�I</font></b>";
		} else {
			$comment .= "<b><font size=5>�ӂ�ɍ���͌�����Ȃ������E�E�E�B</font></b>";
		}
	}

	&acs_sub;

	&levelup;

	&hp_after;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>���e�̏�</B></FONT>
<BR>

<B><CENTER><FONT SIZE= "6">$mname</B>�����ꂽ�I</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}
	
	&mons_footer;

	&footer;

	exit;
}

#----------------------#
#  �ِ��E�ł̐퓬      #
#----------------------#
sub isekiai {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if (!$chara[25]) {
		&error("��x�L�����N�^�[�Ɠ����Ă�������");
	}

	&time_check;

	&item_load;

	&acs_add;

	open(IN,"$isekai_monster");
	@MONSTER = <IN>;
	close(IN);

	$r_no = @MONSTER;

	$r_no = int(rand($r_no));

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

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;

	&acs_sub;

	&levelup;

	&hp_after;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>�ِ��E</B></FONT>
<BR>

<B><CENTER><FONT SIZE= "6">$mname</B>�����ꂽ�I</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&mons_footer;

	&footer;

	exit;
}

