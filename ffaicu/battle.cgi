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
#     http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi 		#
#---------------------------------------------------------------#
# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �퓬���C�u�����̓ǂݍ���
require 'battle.pl';
# �`�����v��p���C�u�����ǂݍ���
require 'wbattle.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $battle_back;
$midi = $battle_midi;


#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

&battle;

exit;

#------------#
#  �퓬���  #
#------------#
sub battle {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	$lock_file = "$lockfolder/cmp.lock";
	&lock($lock_file,'BT');
	&read_winner;

	# �܋��̌���
	$gold = $winner[50];

	if ($winner[0] eq $chara[0]) {
		&error("���݃`�����v�Ȃ̂œ����܂���B");
	}

	$ltime = time();
	$ltime = $ltime - $chara[27];
	$vtime = $b_time - $ltime;

	if ($vtime > 0) {
		&error("����$vtime�b�ԓ����܂���B");
	}

	&item_load;

	&acs_add;

	&wacs_add;

	$khp_flg = $chara[15];
	$whp_flg = $winner[15];

	$i=1;$j=0;@battle_date=();
	foreach (1..$turn) {

		&shokika;

		&tyousensya;
		&winner_atack;

		&tyosenwaza;
		&winwaza;

		&acs_waza;
		&wacs_waza;

		&battle_clt;
		&battle_kaihi;

		&battle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;
	$chara[25] = $sentou_limit;
	$chara[28] = $boss;

	&acs_sub;
	&wacs_sub;

	&levelup;

	$chara[15] = $khp_flg + int(rand($chara[10]));
	if($chara[15] > $chara[16]) { $chara[15] = $chara[16]; }
	$winner[15] = $whp_flg + int(rand($winner[9]));
	if($winner[15] > $winner[16]) { $winner[15] = $winner[16]; }
	if($chara[15] <= 0) { $chara[15] = 1; }
	if($winner[15] <= 0) { $winner[15] = 1; }
	$chara[19] += $gold;
	if($chara[19] < 0){$chara[19] = 0;}
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	if ($win == 1 or $win == 2) {
		$new_winner = "$chara[0]<>$chara[2]<>$chara[3]<>$chara[4]<>$chara[5]<>$chara[6]<>$chara[7]<>$chara[8]<>$chara[9]<>$chara[10]<>$chara[11]<>$chara[12]<>$chara[13]<>$chara[20]<>$chara[14]<>$chara[15]<>$chara[16]<>$chara[18]<>$chara[21]<>$chara[22]<>$chara[23]<>$item[0]<>$item[1]<>$item[2]<>$item[3]<>$item[4]<>$item[5]<>$item[6]<>$item[8]<>$item[9]<>$item[10]<>$item[11]<>$item[12]<>$item[13]<>$item[15]<>$item[17]<>$item[18]<>$chara[30]<>$host<>$chara[33]<>$winner[0]<>$winner[3]<>$winner[1]<>$winner[2]<>1<>$winner[45]<>$winner[46]<>$winner[47]<>$winner[48]<>$winner[49]<>$winner[50]<>$item[7]<>$item[16]<>$item[14]<>";

	} else {
		$winner[44] += 1;

		if ($winner[44] > $winner[45]) {
			$winner[45] = $winner[44];
			$winner[46] = $winner[0];
			$winner[47] = $winner[3];
			$winner[48] = $winner[1];
			$winner[49] = $winner[2];
		}

		$winner[15] += int($winner[16] / 10);
		if($winner[15] > $winner[16]){$winner[15] = $winner[16];}
		$winner[40] = $chara[0];
		$winner[41] = $chara[4];
		$winner[42] = $chara[2];
		$winner[43] = $chara[3];

		$new_winner = '';
		$new_winner = join('<>',@winner);
		$new_winner .= '<>';
	}

	open(OUT,">$winner_file");
	print OUT $new_winner;
	close(OUT);

	$lock_file = "$lockfolder/cmp.lock";
	&unlock($lock_file,'BT');

	if($chara[15] == 1) { $chara[15] = $chara[16]; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print "<h1>$chara[4]�́A$winner[3]�ɐ킢�𒧂񂾁I�I</h1>\n<hr size=0><br>\n";

	$i=0;
	foreach(@battle_date){
		print "$battle_date[$i]";
		$i++;
	}
	
	if ($win) {
		print "$comment<br>$chara[4]�́A<b>$exp</b>�̌o���l����ɓ��ꂽ�B$winner[3]�̏܋�<b>$gold</b>G��ɓ��ꂽ�B<br>\n";
	} else {
		print "$comment<br>$chara[4]�́A<b>$exp</b>�̌o���l����ɓ��ꂽ�B�����������ɂȂ����E�E�E(��)<br>\n";
	}

	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}
