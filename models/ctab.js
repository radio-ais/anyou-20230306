/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('ctab', {
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
    }
  }, {
    sequelize,
    tableName: 'ctab'
  });
};
