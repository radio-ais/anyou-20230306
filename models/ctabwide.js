/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('ctabwide', {
    id: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    createdat: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.fn('current_timestamp')
    },
    updatedat: {
      type: DataTypes.DATE,
      allowNull: true
    },
    sct_ab_desc: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sct_ab_num: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sct_epi_loc: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sct_long_dia: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sct_margins: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sct_perp_dia: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sct_pre_att: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    study_yr: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sct_slice_num: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sct_found_after_comp: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    pid: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    dataset_version: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    sctabdesc: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sctabnum: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sctepiloc: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sctlongdia: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sctmargins: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sctperpdia: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sctpreatt: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    studyyr: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    sctslicenum: {
      type: DataTypes.INTEGER(11),
      allowNull: true
    },
    sctfoundaftercomp: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    datasetversion: {
      type: DataTypes.STRING(100),
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'ctabwide'
  });
};
